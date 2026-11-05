# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T18:22:33.985545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3145` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.7135` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.4105` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.8567` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0415` n `13`; crypto_alt avg `0.6495` n `239`; crypto_major avg `0.3768` n `8`; equity avg `0.4334` n `158`; fx avg `0.003` n `6`; index avg `0.0191` n `27`; metal avg `0.0069` n `20`; unknown avg `0.4047` n `1256`
- 1h: commodity avg `0.0849` n `13`; crypto_alt avg `0.205` n `239`; crypto_major avg `-0.2295` n `8`; equity avg `-0.6341` n `158`; fx avg `0.0114` n `6`; index avg `-0.1078` n `27`; metal avg `-0.129` n `20`; unknown avg `-0.383` n `1254`
- 4h: commodity avg `0.1874` n `13`; crypto_alt avg `-4.2272` n `239`; crypto_major avg `-4.1271` n `8`; equity avg `-5.9838` n `158`; fx avg `0.0786` n `6`; index avg `-0.7166` n `27`; metal avg `-0.4136` n `20`; unknown avg `7.163` n `1246`
- 24h: commodity avg `0.5913` n `13`; crypto_alt avg `-5.3401` n `239`; crypto_major avg `-5.548` n `8`; equity avg `-8.16` n `158`; fx avg `0.1135` n `6`; index avg `-1.1026` n `27`; metal avg `0.1961` n `20`; unknown avg `214.1071` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1822`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
