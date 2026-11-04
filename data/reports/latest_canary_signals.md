# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T17:37:29.630247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.564` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.4749` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7297` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.5137` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1154` n `13`; crypto_alt avg `-0.0746` n `239`; crypto_major avg `-0.1771` n `8`; equity avg `-0.0436` n `158`; fx avg `0.0024` n `6`; index avg `-0.0125` n `27`; metal avg `0.0556` n `20`; unknown avg `18.4915` n `1264`
- 1h: commodity avg `-0.559` n `13`; crypto_alt avg `-0.7577` n `239`; crypto_major avg `-0.6311` n `8`; equity avg `0.8826` n `158`; fx avg `-0.002` n `6`; index avg `0.1109` n `27`; metal avg `0.1615` n `20`; unknown avg `0.6069` n `1258`
- 4h: commodity avg `-1.4729` n `13`; crypto_alt avg `1.2144` n `239`; crypto_major avg `2.0911` n `8`; equity avg `-0.3838` n `158`; fx avg `-0.0464` n `6`; index avg `0.1147` n `27`; metal avg `0.3614` n `20`; unknown avg `19.5594` n `1252`
- 24h: commodity avg `-1.868` n `13`; crypto_alt avg `1.9503` n `239`; crypto_major avg `2.0415` n `8`; equity avg `-0.4759` n `158`; fx avg `0.0657` n `6`; index avg `0.1725` n `27`; metal avg `1.265` n `20`; unknown avg `0.2163` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2714`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
