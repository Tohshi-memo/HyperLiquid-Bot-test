# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T14:07:27.116535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `0.0399` n `239`; crypto_major avg `-0.0609` n `8`; equity avg `-0.031` n `158`; fx avg `0.0037` n `6`; index avg `0.017` n `27`; metal avg `-0.0014` n `20`; unknown avg `1.199` n `1258`
- 1h: commodity avg `0.0063` n `13`; crypto_alt avg `-0.4343` n `239`; crypto_major avg `-0.3133` n `8`; equity avg `-0.0809` n `158`; fx avg `-0.0276` n `6`; index avg `0.0186` n `27`; metal avg `-0.0071` n `20`; unknown avg `1.1318` n `1256`
- 4h: commodity avg `0.028` n `13`; crypto_alt avg `-0.5474` n `239`; crypto_major avg `0.0555` n `8`; equity avg `-0.0202` n `158`; fx avg `-0.0069` n `6`; index avg `0.0091` n `27`; metal avg `-0.0031` n `20`; unknown avg `1.3914` n `1250`
- 24h: commodity avg `0.1108` n `13`; crypto_alt avg `-1.8577` n `239`; crypto_major avg `-0.4461` n `8`; equity avg `0.1027` n `158`; fx avg `0.0159` n `6`; index avg `0.0208` n `27`; metal avg `-0.046` n `20`; unknown avg `6.1561` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
