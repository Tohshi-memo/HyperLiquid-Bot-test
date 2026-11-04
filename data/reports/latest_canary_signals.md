# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T17:22:29.956919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7791` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.224` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9657` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0958` n `13`; crypto_alt avg `-0.5033` n `239`; crypto_major avg `-0.2157` n `8`; equity avg `0.2134` n `158`; fx avg `0.004` n `6`; index avg `0.0167` n `27`; metal avg `-0.0223` n `20`; unknown avg `0.0033` n `1264`
- 1h: commodity avg `-0.8447` n `13`; crypto_alt avg `-0.8037` n `239`; crypto_major avg `-0.602` n `8`; equity avg `0.8379` n `158`; fx avg `-0.0127` n `6`; index avg `0.126` n `27`; metal avg `0.1815` n `20`; unknown avg `4.5327` n `1258`
- 4h: commodity avg `-1.5111` n `13`; crypto_alt avg `1.3245` n `239`; crypto_major avg `2.268` n `8`; equity avg `0.044` n `158`; fx avg `-0.0484` n `6`; index avg `0.1301` n `27`; metal avg `0.3023` n `20`; unknown avg `1.198` n `1252`
- 24h: commodity avg `-1.7883` n `13`; crypto_alt avg `1.778` n `239`; crypto_major avg `2.0524` n `8`; equity avg `-0.5237` n `158`; fx avg `0.0653` n `6`; index avg `0.1655` n `27`; metal avg `1.1653` n `20`; unknown avg `0.3208` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2691`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
