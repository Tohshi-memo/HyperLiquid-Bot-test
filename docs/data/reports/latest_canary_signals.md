# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T18:37:58.100212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.9389` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.3894` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.0773` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `0.3731` n `239`; crypto_major avg `0.0225` n `8`; equity avg `0.0221` n `158`; fx avg `-0.0019` n `6`; index avg `0.0072` n `27`; metal avg `0.0515` n `20`; unknown avg `1.4666` n `1256`
- 1h: commodity avg `0.0716` n `13`; crypto_alt avg `0.4419` n `239`; crypto_major avg `-0.1684` n `8`; equity avg `-0.3389` n `158`; fx avg `0.0096` n `6`; index avg `-0.0627` n `27`; metal avg `-0.0152` n `20`; unknown avg `0.9429` n `1254`
- 4h: commodity avg `0.2836` n `13`; crypto_alt avg `-3.3662` n `239`; crypto_major avg `-3.6553` n `8`; equity avg `-4.3919` n `158`; fx avg `0.0998` n `6`; index avg `-0.578` n `27`; metal avg `-0.2659` n `20`; unknown avg `4.5508` n `1242`
- 24h: commodity avg `0.6654` n `13`; crypto_alt avg `-4.8502` n `239`; crypto_major avg `-5.2698` n `8`; equity avg `-8.083` n `158`; fx avg `0.1332` n `6`; index avg `-1.0716` n `27`; metal avg `0.2922` n `20`; unknown avg `47.7872` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1705`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
