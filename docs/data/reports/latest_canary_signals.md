# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T11:37:23.551057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `13`; crypto_alt avg `0.2822` n `235`; crypto_major avg `0.0956` n `8`; equity avg `0.0074` n `143`; fx avg `0.0009` n `6`; index avg `-0.0004` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.002` n `984`
- 1h: commodity avg `0.073` n `13`; crypto_alt avg `0.1176` n `235`; crypto_major avg `0.0161` n `8`; equity avg `-0.0113` n `143`; fx avg `-0.0043` n `6`; index avg `-0.013` n `26`; metal avg `0.0025` n `20`; unknown avg `-0.0342` n `982`
- 4h: commodity avg `-0.0055` n `13`; crypto_alt avg `0.6691` n `235`; crypto_major avg `0.0819` n `8`; equity avg `0.0183` n `143`; fx avg `-0.0188` n `6`; index avg `-0.0121` n `26`; metal avg `-0.001` n `20`; unknown avg `1.1916` n `966`
- 24h: commodity avg `0.6831` n `13`; crypto_alt avg `-1.7477` n `235`; crypto_major avg `-2.4449` n `8`; equity avg `0.207` n `142`; fx avg `0.0209` n `6`; index avg `0.1083` n `26`; metal avg `-0.2808` n `20`; unknown avg `-0.3992` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
