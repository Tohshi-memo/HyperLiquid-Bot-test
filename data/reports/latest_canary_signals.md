# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T21:00:50.571882+00:00`
- Correlation status: `ready`
- Asset price records: `392`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0687` n `7`; crypto_alt avg `0.1312` n `223`; crypto_major avg `0.0256` n `7`; equity avg `-0.0448` n `47`; fx avg `0.0034` n `4`; index avg `0.0007` n `6`; metal avg `0.0145` n `7`; unknown avg `0.0162` n `313`
- 1h: commodity avg `-0.0069` n `7`; crypto_alt avg `0.7467` n `223`; crypto_major avg `0.2586` n `7`; equity avg `0.1818` n `47`; fx avg `-0.0093` n `4`; index avg `0.107` n `6`; metal avg `0.0577` n `7`; unknown avg `-0.0116` n `313`
- 4h: commodity avg `-0.1191` n `7`; crypto_alt avg `1.3813` n `223`; crypto_major avg `0.901` n `7`; equity avg `0.259` n `47`; fx avg `0.0207` n `4`; index avg `0.2116` n `6`; metal avg `-0.2668` n `7`; unknown avg `0.2584` n `313`
- 24h: commodity avg `-1.1885` n `7`; crypto_alt avg `2.9541` n `223`; crypto_major avg `2.8547` n `7`; equity avg `2.0629` n `47`; fx avg `-0.0477` n `4`; index avg `1.4341` n `6`; metal avg `0.6756` n `7`; unknown avg `1.3569` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2068`, n `388`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2`, n `388`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `388`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `388`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1126`, n `384`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `388`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `388`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1047`, n `384`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `388`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `388`, weak_sample_signal
