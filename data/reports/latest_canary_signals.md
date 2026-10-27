# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T20:23:10.508422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `13`; crypto_alt avg `-0.0488` n `238`; crypto_major avg `-0.0779` n `8`; equity avg `-0.0292` n `154`; fx avg `-0.0087` n `6`; index avg `-0.0165` n `27`; metal avg `-0.0108` n `20`; unknown avg `0.828` n `1176`
- 1h: commodity avg `0.1555` n `13`; crypto_alt avg `-0.0329` n `238`; crypto_major avg `0.0124` n `8`; equity avg `-0.249` n `154`; fx avg `-0.0124` n `6`; index avg `-0.0148` n `27`; metal avg `0.0125` n `20`; unknown avg `0.8211` n `1154`
- 4h: commodity avg `0.0865` n `13`; crypto_alt avg `0.1769` n `238`; crypto_major avg `0.2449` n `8`; equity avg `-0.233` n `154`; fx avg `-0.0061` n `6`; index avg `-0.078` n `27`; metal avg `0.0474` n `20`; unknown avg `1.2857` n `1154`
- 24h: commodity avg `-0.2355` n `13`; crypto_alt avg `1.2436` n `237`; crypto_major avg `1.4957` n `8`; equity avg `1.6412` n `154`; fx avg `-0.0562` n `6`; index avg `0.4255` n `27`; metal avg `0.2101` n `20`; unknown avg `23.6665` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2323`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1977`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
