# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T09:52:32.831933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0379` n `13`; crypto_alt avg `0.041` n `239`; crypto_major avg `0.1671` n `8`; equity avg `0.2119` n `160`; fx avg `0.0007` n `6`; index avg `0.0202` n `27`; metal avg `-0.018` n `20`; unknown avg `0.1233` n `1262`
- 1h: commodity avg `-0.1032` n `13`; crypto_alt avg `-0.0107` n `239`; crypto_major avg `-0.0896` n `8`; equity avg `0.1306` n `160`; fx avg `-0.0369` n `6`; index avg `-0.0112` n `27`; metal avg `-0.1665` n `20`; unknown avg `50.0458` n `1244`
- 4h: commodity avg `-0.5755` n `13`; crypto_alt avg `-0.2737` n `239`; crypto_major avg `-0.8215` n `8`; equity avg `0.064` n `160`; fx avg `-0.0258` n `6`; index avg `-0.0259` n `27`; metal avg `-0.3011` n `20`; unknown avg `20.6465` n `1201`
- 24h: commodity avg `-1.0347` n `13`; crypto_alt avg `1.0236` n `239`; crypto_major avg `0.2299` n `8`; equity avg `4.7201` n `160`; fx avg `-0.0685` n `6`; index avg `0.5088` n `27`; metal avg `0.0484` n `20`; unknown avg `5.9412` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2336`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
