# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T17:52:31.308901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.422` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.3203` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8488` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.2194` n `13`; crypto_alt avg `-0.043` n `239`; crypto_major avg `0.0543` n `8`; equity avg `-0.0156` n `158`; fx avg `-0.0117` n `6`; index avg `0.0104` n `27`; metal avg `-0.0061` n `20`; unknown avg `0.9224` n `1264`
- 1h: commodity avg `0.0568` n `13`; crypto_alt avg `-0.9734` n `239`; crypto_major avg `-0.6615` n `8`; equity avg `0.1616` n `158`; fx avg `0.011` n `6`; index avg `0.007` n `27`; metal avg `0.0998` n `20`; unknown avg `0.1445` n `1258`
- 4h: commodity avg `-1.2502` n `13`; crypto_alt avg `1.2184` n `239`; crypto_major avg `2.1718` n `8`; equity avg `-0.1485` n `158`; fx avg `-0.0633` n `6`; index avg `0.1134` n `27`; metal avg `0.323` n `20`; unknown avg `0.7545` n `1252`
- 24h: commodity avg `-1.6596` n `13`; crypto_alt avg `1.9132` n `239`; crypto_major avg `1.9646` n `8`; equity avg `-0.5361` n `158`; fx avg `0.0532` n `6`; index avg `0.1571` n `27`; metal avg `1.2343` n `20`; unknown avg `0.2801` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2742`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
