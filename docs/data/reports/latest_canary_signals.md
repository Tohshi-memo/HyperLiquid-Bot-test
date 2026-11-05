# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T19:08:26.467323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2269` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9761` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7411` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0389` n `13`; crypto_alt avg `-0.1254` n `239`; crypto_major avg `-0.2204` n `8`; equity avg `0.0014` n `158`; fx avg `0.0035` n `6`; index avg `-0.0242` n `27`; metal avg `-0.0126` n `20`; unknown avg `6.3743` n `1250`
- 1h: commodity avg `-0.0611` n `13`; crypto_alt avg `0.974` n `239`; crypto_major avg `0.1959` n `8`; equity avg `0.3261` n `158`; fx avg `-0.0162` n `6`; index avg `-0.0133` n `27`; metal avg `0.0093` n `20`; unknown avg `6.5339` n `1254`
- 4h: commodity avg `0.0641` n `13`; crypto_alt avg `-1.8494` n `239`; crypto_major avg `-2.1628` n `8`; equity avg `-2.7028` n `158`; fx avg `0.0574` n `6`; index avg `-0.4217` n `27`; metal avg `-0.1867` n `20`; unknown avg `8.1011` n `1244`
- 24h: commodity avg `0.7298` n `13`; crypto_alt avg `-4.9262` n `239`; crypto_major avg `-5.3851` n `8`; equity avg `-8.2957` n `158`; fx avg `0.1126` n `6`; index avg `-1.1287` n `27`; metal avg `0.2277` n `20`; unknown avg `240.3046` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1838`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
