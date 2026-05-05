# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T10:45:27.361637+00:00`
- Correlation status: `ready`
- Asset price records: `353`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `7`; crypto_alt avg `0.0884` n `223`; crypto_major avg `0.1245` n `7`; equity avg `-0.0969` n `47`; fx avg `-0.0019` n `4`; index avg `0.0719` n `6`; metal avg `-0.1387` n `7`; unknown avg `0.0843` n `312`
- 1h: commodity avg `0.0887` n `7`; crypto_alt avg `0.3673` n `223`; crypto_major avg `0.3805` n `7`; equity avg `-0.1727` n `47`; fx avg `0.0071` n `4`; index avg `0.1169` n `6`; metal avg `-0.2628` n `7`; unknown avg `0.0628` n `312`
- 4h: commodity avg `-0.1534` n `7`; crypto_alt avg `0.7006` n `223`; crypto_major avg `0.2346` n `7`; equity avg `-0.0002` n `47`; fx avg `0.0674` n `4`; index avg `0.1479` n `6`; metal avg `0.1955` n `7`; unknown avg `0.2609` n `312`
- 24h: commodity avg `0.155` n `7`; crypto_alt avg `2.2724` n `223`; crypto_major avg `1.6199` n `7`; equity avg `0.5911` n `47`; fx avg `0.0409` n `4`; index avg `0.4561` n `6`; metal avg `0.395` n `7`; unknown avg `-0.4513` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2171`, n `349`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.21`, n `349`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `349`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1344`, n `349`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `349`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1124`, n `349`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `349`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `349`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1025`, n `345`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0998`, n `345`, weak_sample_signal
