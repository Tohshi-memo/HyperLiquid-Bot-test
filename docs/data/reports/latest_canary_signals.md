# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T15:22:32.662869+00:00`
- Correlation status: `ready`
- Asset price records: `465`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `9.33` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.9136` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.605` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2064` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `0.1247` n `228`; crypto_major avg `0.1891` n `8`; equity avg `0.1199` n `65`; fx avg `0.0217` n `4`; index avg `0.0766` n `23`; metal avg `0.0595` n `18`; unknown avg `0.0782` n `356`
- 1h: commodity avg `0.0253` n `12`; crypto_alt avg `0.7005` n `228`; crypto_major avg `0.2761` n `8`; equity avg `0.7427` n `65`; fx avg `0.0201` n `4`; index avg `0.4586` n `23`; metal avg `0.0519` n `18`; unknown avg `0.2189` n `356`
- 4h: commodity avg `1.2677` n `7`; crypto_alt avg `-1.099` n `223`; crypto_major avg `-1.6459` n `7`; equity avg `-0.9316` n `47`; fx avg `0.1023` n `4`; index avg `-0.4395` n `6`; metal avg `-0.0409` n `7`; unknown avg `8.3629` n `313`
- 24h: commodity avg `-2.4265` n `7`; crypto_alt avg `2.7637` n `223`; crypto_major avg `0.9574` n `7`; equity avg `2.2649` n `47`; fx avg `-0.4539` n `4`; index avg `1.9687` n `6`; metal avg `2.8843` n `7`; unknown avg `19.615` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.3025`, n `461`, moderate_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.2204`, n `461`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.201`, n `457`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1947`, n `457`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1755`, n `457`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1719`, n `457`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1396`, n `461`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1379`, n `461`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1373`, n `461`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1361`, n `461`, weak_sample_signal
