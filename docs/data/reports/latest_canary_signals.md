# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T00:37:22.339881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `13`; crypto_alt avg `-0.0554` n `239`; crypto_major avg `-0.1072` n `8`; equity avg `-0.1583` n `168`; fx avg `-0.0092` n `6`; index avg `-0.0244` n `27`; metal avg `0.009` n `20`; unknown avg `1.9249` n `1241`
- 1h: commodity avg `0.03` n `13`; crypto_alt avg `-0.2391` n `239`; crypto_major avg `-0.3149` n `8`; equity avg `-0.6094` n `168`; fx avg `0.0547` n `6`; index avg `-0.0741` n `27`; metal avg `-0.1225` n `20`; unknown avg `84.342` n `1227`
- 4h: commodity avg `0.1004` n `13`; crypto_alt avg `0.2012` n `239`; crypto_major avg `0.3388` n `8`; equity avg `-0.1464` n `168`; fx avg `0.0425` n `6`; index avg `-0.0193` n `27`; metal avg `0.0055` n `20`; unknown avg `2.3895` n `1135`
- 24h: commodity avg `0.596` n `13`; crypto_alt avg `-3.0903` n `239`; crypto_major avg `-2.5706` n `8`; equity avg `-4.7392` n `167`; fx avg `0.2504` n `6`; index avg `-0.4007` n `27`; metal avg `-1.3116` n `20`; unknown avg `446.011` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
