# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T20:07:29.835286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0607` n `13`; crypto_alt avg `0.0454` n `238`; crypto_major avg `0.0198` n `8`; equity avg `-0.0963` n `154`; fx avg `-0.0043` n `6`; index avg `0.0117` n `27`; metal avg `0.0095` n `20`; unknown avg `-0.075` n `1216`
- 1h: commodity avg `0.2072` n `13`; crypto_alt avg `-0.0344` n `238`; crypto_major avg `-0.0256` n `8`; equity avg `-0.2501` n `154`; fx avg `0.0009` n `6`; index avg `0.0051` n `27`; metal avg `0.0472` n `20`; unknown avg `4.3307` n `1216`
- 4h: commodity avg `0.0632` n `13`; crypto_alt avg `0.3683` n `238`; crypto_major avg `0.4021` n `8`; equity avg `-0.1392` n `154`; fx avg `-0.0026` n `6`; index avg `-0.0117` n `27`; metal avg `0.0355` n `20`; unknown avg `0.5254` n `1216`
- 24h: commodity avg `-0.2959` n `13`; crypto_alt avg `1.304` n `237`; crypto_major avg `1.4546` n `8`; equity avg `1.8031` n `154`; fx avg `-0.0512` n `6`; index avg `0.4471` n `27`; metal avg `0.2338` n `20`; unknown avg `26.4061` n `1052`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2318`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
