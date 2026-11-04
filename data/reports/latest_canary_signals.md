# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T18:07:30.449195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7346` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.6834` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.2638` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0181` n `13`; crypto_alt avg `0.2899` n `239`; crypto_major avg `0.3517` n `8`; equity avg `-0.0953` n `158`; fx avg `0.0076` n `6`; index avg `-0.0005` n `27`; metal avg `0.0352` n `20`; unknown avg `0.3175` n `1258`
- 1h: commodity avg `0.0807` n `13`; crypto_alt avg `-0.2656` n `239`; crypto_major avg `0.0282` n `8`; equity avg `0.1721` n `158`; fx avg `0.0044` n `6`; index avg `0.021` n `27`; metal avg `0.0522` n `20`; unknown avg `-0.0918` n `1258`
- 4h: commodity avg `-1.1214` n `13`; crypto_alt avg `1.7802` n `239`; crypto_major avg `2.6132` n `8`; equity avg `-0.0702` n `158`; fx avg `-0.0491` n `6`; index avg `0.1385` n `27`; metal avg `0.3494` n `20`; unknown avg `0.576` n `1250`
- 24h: commodity avg `-1.6055` n `13`; crypto_alt avg `1.9884` n `239`; crypto_major avg `2.1253` n `8`; equity avg `-0.7411` n `158`; fx avg `0.0559` n `6`; index avg `0.1341` n `27`; metal avg `1.221` n `20`; unknown avg `0.2195` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2718`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
