using System;
using IronPython.Hosting;
using System.Collections.Generic;
using Microsoft.Scripting.Hosting;

namespace TickerTape
{
    class Program
    {
        static void Main(string[] args)
        {

            ScriptEngine pythonEngine = Python.CreateEngine();
            ScriptSource pythonScript = pythonEngine.CreateScriptSourceFromString("print 'Hello World!'");
            pythonScript.Execute();

            //Console.WriteLine("Hello World!");
        }

        //public string PatchParameter(string parameter, int serviceid)
        //{
        //    var engine = Python.CreateEngine();
        //    var scope = engine.CreateScope();
        //    var d = new Dictionary<string, object>
        //    {
        //        { "serviceid", serviceid},
        //        { "parameter", parameter}
        //    }; // Add some sample parameters. Notice that there is no need in specifically setting the object type, interpreter will do that part for us in the script properly with high probability

        //    //scope.SetVariable("params", d); // This will be the name of the dictionary in python script, initialized with previously created .NET Dictionary
        //    //ScriptSource source = engine.CreateScriptSourceFromFile("PATH_TO_PYTHON_SCRIPT_FILE"); // Load the script
        //    //object result = source.Execute(scope);
        //    //parameter = scope.GetVariable<string>("parameter"); // To get the finally set variable 'parameter' from the python script
        //    //return parameter;
        //}


    }
}
