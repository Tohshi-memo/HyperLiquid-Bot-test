# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T16:07:31.109429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `4.5259` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.2286` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4164` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.8931` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.3212` n `13`; crypto_alt avg `-0.2762` n `239`; crypto_major avg `0.1801` n `8`; equity avg `-0.4674` n `158`; fx avg `-0.0034` n `6`; index avg `-0.0446` n `27`; metal avg `0.012` n `20`; unknown avg `-0.0443` n `1252`
- 1h: commodity avg `-0.3623` n `13`; crypto_alt avg `-0.5755` n `239`; crypto_major avg `-0.3596` n `8`; equity avg `-2.2527` n `158`; fx avg `-0.0243` n `6`; index avg `-0.174` n `27`; metal avg `0.0435` n `20`; unknown avg `0.0445` n `1250`
- 4h: commodity avg `-0.682` n `13`; crypto_alt avg `1.5933` n `239`; crypto_major avg `2.5466` n `8`; equity avg `-1.9793` n `158`; fx avg `-0.0195` n `6`; index avg `-0.0703` n `27`; metal avg `0.1302` n `20`; unknown avg `0.4971` n `1250`
- 24h: commodity avg `-0.7929` n `13`; crypto_alt avg `2.3927` n `239`; crypto_major avg `2.6047` n `8`; equity avg `-1.8094` n `158`; fx avg `0.094` n `6`; index avg `-0.033` n `27`; metal avg `0.9472` n `20`; unknown avg `-0.011` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2625`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
