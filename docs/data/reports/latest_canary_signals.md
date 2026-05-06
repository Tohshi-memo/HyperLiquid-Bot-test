# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T08:45:31.925148+00:00`
- Correlation status: `ready`
- Asset price records: `439`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0953` n `7`; crypto_alt avg `0.2522` n `223`; crypto_major avg `0.2628` n `7`; equity avg `0.0852` n `47`; fx avg `-0.0274` n `4`; index avg `-0.222` n `6`; metal avg `-0.0791` n `7`; unknown avg `-0.0295` n `313`
- 1h: commodity avg `-0.3279` n `7`; crypto_alt avg `0.73` n `223`; crypto_major avg `0.4453` n `7`; equity avg `0.3843` n `47`; fx avg `-0.0834` n `4`; index avg `0.092` n `6`; metal avg `0.0595` n `7`; unknown avg `-0.0962` n `313`
- 4h: commodity avg `-0.4558` n `7`; crypto_alt avg `1.5258` n `223`; crypto_major avg `1.0427` n `7`; equity avg `0.4132` n `47`; fx avg `0.0169` n `4`; index avg `-0.1004` n `6`; metal avg `0.2857` n `7`; unknown avg `1.1148` n `311`
- 24h: commodity avg `-1.7172` n `7`; crypto_alt avg `3.6187` n `223`; crypto_major avg `2.6201` n `7`; equity avg `2.898` n `47`; fx avg `-0.4868` n `4`; index avg `1.8672` n `6`; metal avg `1.9801` n `7`; unknown avg `2.1314` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.178`, n `435`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1718`, n `435`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1335`, n `435`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1241`, n `435`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `435`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `435`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.098`, n `431`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0929`, n `431`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `435`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `435`, weak_sample_signal
