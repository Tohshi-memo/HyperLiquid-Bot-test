# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T15:07:26.724979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0769` n `12`; crypto_alt avg `-0.0384` n `228`; crypto_major avg `-0.099` n `8`; equity avg `-0.0495` n `86`; fx avg `-0.0311` n `6`; index avg `-0.0118` n `23`; metal avg `-0.1111` n `20`; unknown avg `-0.0009` n `765`
- 1h: commodity avg `-0.0859` n `12`; crypto_alt avg `0.0612` n `228`; crypto_major avg `0.0061` n `8`; equity avg `-0.1235` n `86`; fx avg `-0.0457` n `6`; index avg `-0.0259` n `23`; metal avg `-0.0205` n `20`; unknown avg `-0.0219` n `765`
- 4h: commodity avg `-0.2291` n `12`; crypto_alt avg `0.7571` n `228`; crypto_major avg `0.8579` n `8`; equity avg `0.8238` n `86`; fx avg `-0.0335` n `6`; index avg `0.0928` n `23`; metal avg `0.2209` n `20`; unknown avg `0.0442` n `765`
- 24h: commodity avg `-0.4356` n `12`; crypto_alt avg `1.2159` n `228`; crypto_major avg `2.1395` n `8`; equity avg `-0.8398` n `86`; fx avg `-0.027` n `6`; index avg `-0.2712` n `23`; metal avg `0.6341` n `20`; unknown avg `0.048` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3898`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.264`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2303`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
