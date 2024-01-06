using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using Newtonsoft.Json;
using OfficeOpenXml;

public class ExcelToJson
{
    private static readonly string ExcelFilePath = "/Users/alsidhu/Downloads/TOF.xlsx";

    public static void Main()
    {
        try
        {
            // Set the license context to a proper value
            ExcelPackage.LicenseContext = LicenseContext.NonCommercial;

            string scopeJson = ConvertDataTableToJson("Scope");
            string summaryJson = ConvertDataTableToJson("Summary");

            Console.WriteLine("Scope JSON:");
            Console.WriteLine(scopeJson);

            Console.WriteLine("\nSummary JSON:");
            Console.WriteLine(summaryJson);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    private static string ConvertDataTableToJson(string sheetName)
    {
        using (var package = new ExcelPackage(new FileInfo(ExcelFilePath)))
        {
            ExcelWorksheet worksheet = package.Workbook.Worksheets[sheetName];
            DataTable table = new DataTable(sheetName);

            foreach (var firstRowCell in worksheet.Cells[1, 1, 1, worksheet.Dimension.End.Column])
            {
                table.Columns.Add(firstRowCell.Text);
            }

            for (var rowNumber = 2; rowNumber <= worksheet.Dimension.End.Row; rowNumber++)
            {
                var row = worksheet.Cells[rowNumber, 1, rowNumber, worksheet.Dimension.End.Column];
                var newRow = table.NewRow();

                foreach (var cell in row)
                {
                    int columnIndex = cell.Start.Column - 1;
                    if (columnIndex < table.Columns.Count)
                    {
                        newRow[columnIndex] = cell.Text;
                    }
                }

                table.Rows.Add(newRow);
            }

            List<Dictionary<string, object>> rows = new List<Dictionary<string, object>>();
            foreach (DataRow dr in table.Rows)
            {
                var row = new Dictionary<string, object>();
                foreach (DataColumn col in table.Columns)
                {
                    row[col.ColumnName] = dr[col];
                }
                rows.Add(row);
            }

            return JsonConvert.SerializeObject(rows, Formatting.Indented);
        }
    }
}
