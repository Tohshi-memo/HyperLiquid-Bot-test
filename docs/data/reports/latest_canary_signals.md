# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T19:50:12.343021+00:00`
- Correlation status: `ready`
- Asset price records: `387`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `7`; crypto_alt avg `-0.039` n `223`; crypto_major avg `-0.0492` n `7`; equity avg `0.1123` n `47`; fx avg `-0.016` n `4`; index avg `-0.0325` n `6`; metal avg `-0.0721` n `7`; unknown avg `0.0156` n `313`
- 1h: commodity avg `-0.0055` n `7`; crypto_alt avg `0.1989` n `223`; crypto_major avg `0.0974` n `7`; equity avg `0.058` n `47`; fx avg `-0.003` n `4`; index avg `-0.0219` n `6`; metal avg `-0.2171` n `7`; unknown avg `1.1807` n `313`
- 4h: commodity avg `0.0735` n `7`; crypto_alt avg `0.4417` n `223`; crypto_major avg `0.1474` n `7`; equity avg `-0.0976` n `47`; fx avg `-0.0072` n `4`; index avg `0.1859` n `6`; metal avg `-0.5768` n `7`; unknown avg `1.1225` n `313`
- 24h: commodity avg `-1.2312` n `7`; crypto_alt avg `1.8433` n `223`; crypto_major avg `2.375` n `7`; equity avg `1.7838` n `47`; fx avg `-0.0369` n `4`; index avg `1.4949` n `6`; metal avg `0.6174` n `7`; unknown avg `2.1795` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `383`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2001`, n `383`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1315`, n `383`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1275`, n `383`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1137`, n `379`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `383`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1068`, n `383`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1059`, n `379`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `383`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `383`, weak_sample_signal
