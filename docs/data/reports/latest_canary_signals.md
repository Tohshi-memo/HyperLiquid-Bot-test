# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T15:07:27.042330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.3451` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `3.3442` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.2231` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.7963` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5119` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.0686` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1064` n `13`; crypto_alt avg `0.9521` n `239`; crypto_major avg `1.2693` n `8`; equity avg `0.292` n `158`; fx avg `-0.0167` n `6`; index avg `0.0177` n `27`; metal avg `0.0012` n `20`; unknown avg `4.4549` n `1256`
- 1h: commodity avg `-0.0365` n `13`; crypto_alt avg `2.8336` n `239`; crypto_major avg `3.3077` n `8`; equity avg `1.2391` n `158`; fx avg `-0.0178` n `6`; index avg `0.1647` n `27`; metal avg `0.0846` n `20`; unknown avg `2.3042` n `1256`
- 4h: commodity avg `-0.3142` n `13`; crypto_alt avg `1.8922` n `239`; crypto_major avg `2.4821` n `8`; equity avg `-0.863` n `158`; fx avg `0.0115` n `6`; index avg `0.0525` n `27`; metal avg `-0.0298` n `20`; unknown avg `2.251` n `1250`
- 24h: commodity avg `-0.3945` n `13`; crypto_alt avg `3.2423` n `239`; crypto_major avg `3.2329` n `8`; equity avg `0.7828` n `158`; fx avg `0.1124` n `6`; index avg `0.1949` n `27`; metal avg `0.8486` n `20`; unknown avg `1.2989` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2594`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
