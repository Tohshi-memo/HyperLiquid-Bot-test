# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T14:52:35.750835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.3452` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.1447` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.8597` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0344` n `13`; crypto_alt avg `1.4527` n `239`; crypto_major avg `1.4455` n `8`; equity avg `0.5323` n `158`; fx avg `0.0018` n `6`; index avg `0.0723` n `27`; metal avg `0.0048` n `20`; unknown avg `1.8695` n `1264`
- 1h: commodity avg `-0.2029` n `13`; crypto_alt avg `1.6541` n `239`; crypto_major avg `1.9418` n `8`; equity avg `0.8803` n `158`; fx avg `-0.0057` n `6`; index avg `0.1277` n `27`; metal avg `0.0821` n `20`; unknown avg `2.1683` n `1258`
- 4h: commodity avg `-0.4189` n `13`; crypto_alt avg `0.9291` n `239`; crypto_major avg `1.1933` n `8`; equity avg `-1.1519` n `158`; fx avg `0.0281` n `6`; index avg `0.0348` n `27`; metal avg `-0.0312` n `20`; unknown avg `2.4993` n `1254`
- 24h: commodity avg `-0.5012` n `13`; crypto_alt avg `2.0157` n `239`; crypto_major avg `1.7453` n `8`; equity avg `0.4027` n `158`; fx avg `0.1392` n `6`; index avg `0.1829` n `27`; metal avg `0.81` n `20`; unknown avg `1.7376` n `1089`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2588`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
