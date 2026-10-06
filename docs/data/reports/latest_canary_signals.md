# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T02:52:32.634465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.0336` n `235`; crypto_major avg `-0.0457` n `8`; equity avg `0.0116` n `149`; fx avg `0.0037` n `6`; index avg `0.001` n `26`; metal avg `0.0598` n `20`; unknown avg `0.1137` n `1074`
- 1h: commodity avg `0.0286` n `13`; crypto_alt avg `-0.4199` n `235`; crypto_major avg `-0.2074` n `8`; equity avg `-0.0897` n `149`; fx avg `-0.0168` n `6`; index avg `-0.0157` n `26`; metal avg `0.0068` n `20`; unknown avg `-0.378` n `1072`
- 4h: commodity avg `0.0698` n `13`; crypto_alt avg `-1.5279` n `235`; crypto_major avg `-0.6448` n `8`; equity avg `-0.2111` n `149`; fx avg `0.0032` n `6`; index avg `-0.0619` n `26`; metal avg `-0.0693` n `20`; unknown avg `0.5175` n `1066`
- 24h: commodity avg `-0.0273` n `13`; crypto_alt avg `-1.4557` n `235`; crypto_major avg `-0.6543` n `8`; equity avg `-0.1215` n `149`; fx avg `0.0034` n `6`; index avg `0.0552` n `26`; metal avg `0.0159` n `20`; unknown avg `630.714` n `793`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
