# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T16:30:24.197121+00:00`
- Correlation status: `ready`
- Asset price records: `280`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2164` n `7`; crypto_alt avg `-0.1651` n `223`; crypto_major avg `-0.1735` n `7`; equity avg `-0.1064` n `42`; fx avg `-0.0035` n `4`; index avg `-0.0649` n `9`; metal avg `-0.1371` n `7`; unknown avg `-0.0306` n `314`
- 1h: commodity avg `0.0728` n `7`; crypto_alt avg `0.1473` n `223`; crypto_major avg `0.2541` n `7`; equity avg `-0.5319` n `42`; fx avg `-0.0062` n `4`; index avg `-0.2034` n `9`; metal avg `-0.2914` n `7`; unknown avg `0.2566` n `314`
- 4h: commodity avg `1.2321` n `7`; crypto_alt avg `0.4197` n `223`; crypto_major avg `0.4409` n `7`; equity avg `-0.3963` n `42`; fx avg `-0.0063` n `4`; index avg `0.0302` n `9`; metal avg `-0.98` n `7`; unknown avg `-0.6805` n `314`
- 24h: commodity avg `2.2597` n `7`; crypto_alt avg `1.6794` n `223`; crypto_major avg `1.1264` n `7`; equity avg `-0.1049` n `42`; fx avg `-0.0919` n `4`; index avg `0.5374` n `9`; metal avg `-2.3697` n `7`; unknown avg `-0.6572` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2411`, n `277`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2355`, n `277`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1555`, n `273`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1544`, n `273`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1524`, n `277`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1517`, n `277`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1497`, n `273`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1491`, n `273`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `277`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1431`, n `273`, weak_sample_signal
