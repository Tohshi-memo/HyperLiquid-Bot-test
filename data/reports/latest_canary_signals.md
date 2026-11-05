# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T16:07:26.610011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.9683` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-4.2655` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.8389` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `2.8673` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.648` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.2755` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1714` n `13`; crypto_alt avg `0.725` n `239`; crypto_major avg `0.5133` n `8`; equity avg `0.4553` n `158`; fx avg `-0.0174` n `6`; index avg `0.0206` n `27`; metal avg `-0.0452` n `20`; unknown avg `1.3652` n `1244`
- 1h: commodity avg `0.1449` n `13`; crypto_alt avg `-2.4335` n `239`; crypto_major avg `-1.6003` n `8`; equity avg `-3.2483` n `158`; fx avg `0.0532` n `6`; index avg `-0.3248` n `27`; metal avg `-0.3069` n `20`; unknown avg `2.8742` n `1244`
- 4h: commodity avg `0.3855` n `13`; crypto_alt avg `-5.012` n `239`; crypto_major avg `-4.5828` n `8`; equity avg `-7.4501` n `158`; fx avg `0.0701` n `6`; index avg `-0.7439` n `27`; metal avg `-0.3173` n `20`; unknown avg `7.0056` n `1243`
- 24h: commodity avg `-0.0398` n `13`; crypto_alt avg `-6.273` n `239`; crypto_major avg `-5.5642` n `8`; equity avg `-8.1578` n `158`; fx avg `0.0853` n `6`; index avg `-0.9257` n `27`; metal avg `0.2684` n `20`; unknown avg `229.3676` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2414`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
