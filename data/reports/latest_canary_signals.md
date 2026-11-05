# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T17:37:34.058144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.4456` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.9759` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.4391` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.7453` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `0.1355` n `239`; crypto_major avg `-0.0387` n `8`; equity avg `-0.2756` n `158`; fx avg `0.0` n `6`; index avg `-0.0381` n `27`; metal avg `-0.0624` n `20`; unknown avg `-0.1538` n `1256`
- 1h: commodity avg `0.099` n `13`; crypto_alt avg `-0.7544` n `239`; crypto_major avg `-0.9427` n `8`; equity avg `-1.489` n `158`; fx avg `0.0053` n `6`; index avg `-0.1781` n `27`; metal avg `-0.131` n `20`; unknown avg `-0.8361` n `1254`
- 4h: commodity avg `0.3121` n `13`; crypto_alt avg `-4.4951` n `239`; crypto_major avg `-4.1335` n `8`; equity avg `-5.8788` n `158`; fx avg `0.0838` n `6`; index avg `-0.6944` n `27`; metal avg `-0.1576` n `20`; unknown avg `8.4408` n `1244`
- 24h: commodity avg `0.975` n `13`; crypto_alt avg `-5.3909` n `239`; crypto_major avg `-5.0691` n `8`; equity avg `-8.1178` n `158`; fx avg `0.1019` n `6`; index avg `-1.0467` n `27`; metal avg `0.2541` n `20`; unknown avg `52.6435` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2281`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1857`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1804`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1765`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.175`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1717`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1675`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1663`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1607`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `669`, weak_sample_signal
