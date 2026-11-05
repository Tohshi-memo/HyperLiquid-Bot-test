# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T18:07:33.178652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-5.0493` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-4.3769` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.9614` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.7876` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.3502` n `239`; crypto_major avg `-0.2744` n `8`; equity avg `-0.4259` n `158`; fx avg `-0.0003` n `6`; index avg `-0.0503` n `27`; metal avg `-0.0343` n `20`; unknown avg `-0.1848` n `1250`
- 1h: commodity avg `0.1484` n `13`; crypto_alt avg `-0.2629` n `239`; crypto_major avg `-0.5621` n `8`; equity avg `-0.7389` n `158`; fx avg `0.0098` n `6`; index avg `-0.1099` n `27`; metal avg `-0.2083` n `20`; unknown avg `-0.3912` n `1254`
- 4h: commodity avg `0.3291` n `13`; crypto_alt avg `-5.0252` n `239`; crypto_major avg `-4.7202` n `8`; equity avg `-6.5078` n `158`; fx avg `0.0914` n `6`; index avg `-0.7588` n `27`; metal avg `-0.3433` n `20`; unknown avg `8.489` n `1244`
- 24h: commodity avg `0.7023` n `13`; crypto_alt avg `-6.2086` n `239`; crypto_major avg `-5.9935` n `8`; equity avg `-8.8091` n `158`; fx avg `0.1127` n `6`; index avg `-1.1454` n `27`; metal avg `0.1602` n `20`; unknown avg `235.8824` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
