# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T06:07:31.555151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `13`; crypto_alt avg `-0.059` n `239`; crypto_major avg `0.0987` n `8`; equity avg `0.1961` n `158`; fx avg `-0.0244` n `6`; index avg `0.0261` n `27`; metal avg `-0.045` n `20`; unknown avg `0.0112` n `1231`
- 1h: commodity avg `-0.1378` n `13`; crypto_alt avg `-0.0796` n `239`; crypto_major avg `-0.1909` n `8`; equity avg `-0.1902` n `158`; fx avg `-0.027` n `6`; index avg `-0.0587` n `27`; metal avg `-0.0533` n `20`; unknown avg `-0.1363` n `1225`
- 4h: commodity avg `0.0068` n `13`; crypto_alt avg `-0.7693` n `239`; crypto_major avg `-0.9433` n `8`; equity avg `-0.6525` n `158`; fx avg `-0.0667` n `6`; index avg `-0.0911` n `27`; metal avg `-0.1531` n `20`; unknown avg `0.6495` n `1208`
- 24h: commodity avg `0.0154` n `13`; crypto_alt avg `-2.1896` n `239`; crypto_major avg `-2.8896` n `8`; equity avg `-0.1472` n `158`; fx avg `-0.1382` n `6`; index avg `-0.0233` n `27`; metal avg `0.4318` n `20`; unknown avg `1.5946` n `980`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
