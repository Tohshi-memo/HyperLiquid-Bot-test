# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T17:07:45.410759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.3066` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-4.2045` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.5451` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.627` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0223` n `13`; crypto_alt avg `-1.064` n `239`; crypto_major avg `-0.9458` n `8`; equity avg `-1.5375` n `158`; fx avg `0.0039` n `6`; index avg `-0.1572` n `27`; metal avg `0.0043` n `20`; unknown avg `-0.7829` n `1252`
- 1h: commodity avg `-0.1666` n `13`; crypto_alt avg `-0.1028` n `239`; crypto_major avg `-0.204` n `8`; equity avg `1.0083` n `158`; fx avg `0.0105` n `6`; index avg `0.0245` n `27`; metal avg `0.3231` n `20`; unknown avg `4.8463` n `1254`
- 4h: commodity avg `0.1082` n `13`; crypto_alt avg `-4.6324` n `239`; crypto_major avg `-4.1984` n `8`; equity avg `-5.8254` n `158`; fx avg `0.0694` n `6`; index avg `-0.6533` n `27`; metal avg `0.0061` n `20`; unknown avg `5.9278` n `1243`
- 24h: commodity avg `0.6325` n `13`; crypto_alt avg `-6.2114` n `239`; crypto_major avg `-5.4408` n `8`; equity avg `-8.0153` n `158`; fx avg `0.107` n `6`; index avg `-1.0252` n `27`; metal avg `0.4254` n `20`; unknown avg `345.6713` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2271`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1876`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1772`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1762`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1735`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1734`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1652`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1631`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1602`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1336`, n `669`, weak_sample_signal
