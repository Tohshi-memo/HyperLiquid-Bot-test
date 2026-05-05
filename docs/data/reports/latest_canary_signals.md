# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T05:30:30.615150+00:00`
- Correlation status: `ready`
- Asset price records: `332`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `7`; crypto_alt avg `-0.0264` n `223`; crypto_major avg `0.1291` n `7`; equity avg `0.316` n `47`; fx avg `-0.0058` n `4`; index avg `-0.0033` n `6`; metal avg `0.033` n `7`; unknown avg `1.7588` n `312`
- 1h: commodity avg `0.0302` n `7`; crypto_alt avg `0.0983` n `223`; crypto_major avg `0.1886` n `7`; equity avg `0.5692` n `47`; fx avg `-0.0171` n `4`; index avg `0.0428` n `6`; metal avg `0.1943` n `7`; unknown avg `1.0982` n `312`
- 4h: commodity avg `-0.1768` n `7`; crypto_alt avg `0.3838` n `223`; crypto_major avg `0.716` n `7`; equity avg `0.8601` n `47`; fx avg `-0.0104` n `4`; index avg `0.271` n `6`; metal avg `0.3113` n `7`; unknown avg `2.1388` n `312`
- 24h: commodity avg `1.229` n `7`; crypto_alt avg `0.813` n `223`; crypto_major avg `-0.0865` n `7`; equity avg `-0.2511` n `47`; fx avg `-0.0297` n `4`; index avg `-0.196` n `6`; metal avg `-1.4388` n `7`; unknown avg `0.1599` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.226`, n `328`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2195`, n `328`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `328`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1406`, n `328`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `328`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1245`, n `324`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1215`, n `324`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1211`, n `328`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `328`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1095`, n `328`, weak_sample_signal
