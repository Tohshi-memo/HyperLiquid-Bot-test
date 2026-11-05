# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T17:22:29.565739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3739` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-4.1613` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.5339` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.5189` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0055` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.105` n `13`; crypto_alt avg `0.1791` n `239`; crypto_major avg `0.0419` n `8`; equity avg `0.3274` n `158`; fx avg `0.0013` n `6`; index avg `0.0168` n `27`; metal avg `-0.0729` n `20`; unknown avg `0.1733` n `1256`
- 1h: commodity avg `0.0114` n `13`; crypto_alt avg `-1.1021` n `239`; crypto_major avg `-1.141` n `8`; equity avg `-1.1922` n `158`; fx avg `0.012` n `6`; index avg `-0.1355` n `27`; metal avg `-0.0166` n `20`; unknown avg `3.1926` n `1254`
- 4h: commodity avg `0.1771` n `13`; crypto_alt avg `-4.601` n `239`; crypto_major avg `-4.1968` n `8`; equity avg `-5.7157` n `158`; fx avg `0.0825` n `6`; index avg `-0.6629` n `27`; metal avg `-0.0355` n `20`; unknown avg `6.9463` n `1246`
- 24h: commodity avg `0.8382` n `13`; crypto_alt avg `-5.5835` n `239`; crypto_major avg `-5.1995` n `8`; equity avg `-7.9218` n `158`; fx avg `0.1043` n `6`; index avg `-1.0245` n `27`; metal avg `0.3741` n `20`; unknown avg `324.4963` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2273`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1872`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1788`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1762`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1749`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.173`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1668`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1646`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1606`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1348`, n `669`, weak_sample_signal
