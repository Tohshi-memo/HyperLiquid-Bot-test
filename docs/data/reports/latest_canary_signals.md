# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T04:30:21.672705+00:00`
- Correlation status: `ready`
- Asset price records: `328`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0508` n `7`; crypto_alt avg `0.1025` n `223`; crypto_major avg `-0.0029` n `7`; equity avg `0.0637` n `47`; fx avg `0.0024` n `4`; index avg `0.0752` n `6`; metal avg `0.0029` n `7`; unknown avg `-0.0358` n `312`
- 1h: commodity avg `-0.0341` n `7`; crypto_alt avg `-0.0995` n `223`; crypto_major avg `0.091` n `7`; equity avg `0.1399` n `47`; fx avg `0.0037` n `4`; index avg `0.1186` n `6`; metal avg `-0.0588` n `7`; unknown avg `-0.0773` n `312`
- 4h: commodity avg `-0.2057` n `7`; crypto_alt avg `0.8878` n `223`; crypto_major avg `0.9955` n `7`; equity avg `0.4635` n `47`; fx avg `-0.0003` n `4`; index avg `0.281` n `6`; metal avg `0.4` n `7`; unknown avg `0.2809` n `312`
- 24h: commodity avg `1.0536` n `7`; crypto_alt avg `0.3284` n `223`; crypto_major avg `-0.7122` n `7`; equity avg `-0.817` n `47`; fx avg `0.0039` n `4`; index avg `-0.1212` n `6`; metal avg `-1.9398` n `7`; unknown avg `-1.4387` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2269`, n `324`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2205`, n `324`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.153`, n `324`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1408`, n `320`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1405`, n `324`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1382`, n `320`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `324`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `324`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `324`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `320`, weak_sample_signal
