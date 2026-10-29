# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T23:22:26.413889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0844` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.0268` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8493` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `0.3312` n `238`; crypto_major avg `0.158` n `8`; equity avg `0.1309` n `156`; fx avg `-0.0079` n `6`; index avg `0.0245` n `27`; metal avg `-0.0018` n `20`; unknown avg `-0.1438` n `1260`
- 1h: commodity avg `-0.0314` n `13`; crypto_alt avg `-0.354` n `238`; crypto_major avg `-0.4734` n `8`; equity avg `-0.2364` n `156`; fx avg `0.004` n `6`; index avg `-0.0188` n `27`; metal avg `-0.0569` n `20`; unknown avg `165.6312` n `1252`
- 4h: commodity avg `0.0337` n `13`; crypto_alt avg `-4.5168` n `238`; crypto_major avg `-3.0507` n `8`; equity avg `-2.4578` n `156`; fx avg `0.0314` n `6`; index avg `-0.2014` n `27`; metal avg `-0.0239` n `20`; unknown avg `23.2234` n `1162`
- 24h: commodity avg `-0.2225` n `13`; crypto_alt avg `-5.7203` n `238`; crypto_major avg `-2.2336` n `8`; equity avg `-3.5597` n `155`; fx avg `0.0723` n `6`; index avg `-0.3046` n `27`; metal avg `-0.6356` n `20`; unknown avg `32.1217` n `996`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
