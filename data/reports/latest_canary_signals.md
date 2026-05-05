# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T11:30:25.743939+00:00`
- Correlation status: `ready`
- Asset price records: `356`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1189` n `7`; crypto_alt avg `0.1505` n `223`; crypto_major avg `0.0302` n `7`; equity avg `-0.0158` n `47`; fx avg `0.0084` n `4`; index avg `0.0068` n `6`; metal avg `0.0939` n `7`; unknown avg `0.1117` n `312`
- 1h: commodity avg `0.1376` n `7`; crypto_alt avg `0.0021` n `223`; crypto_major avg `0.3415` n `7`; equity avg `0.1205` n `47`; fx avg `0.0121` n `4`; index avg `-0.0951` n `6`; metal avg `0.0582` n `7`; unknown avg `0.2574` n `312`
- 4h: commodity avg `0.0977` n `7`; crypto_alt avg `0.1235` n `223`; crypto_major avg `0.141` n `7`; equity avg `-0.0626` n `47`; fx avg `0.0878` n `4`; index avg `0.0846` n `6`; metal avg `0.2194` n `7`; unknown avg `0.2764` n `312`
- 24h: commodity avg `0.2975` n `7`; crypto_alt avg `2.4271` n `223`; crypto_major avg `2.098` n `7`; equity avg `0.6329` n `47`; fx avg `0.0675` n `4`; index avg `0.2839` n `6`; metal avg `0.6847` n `7`; unknown avg `-0.2738` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2168`, n `352`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2098`, n `352`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1369`, n `352`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1325`, n `352`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1231`, n `352`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `352`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `352`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1058`, n `348`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `352`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0934`, n `348`, weak_sample_signal
