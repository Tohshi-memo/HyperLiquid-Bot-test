# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T15:22:27.985829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.6543` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.4669` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.42` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.3264` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2686` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-2.2649` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.08` n `13`; crypto_alt avg `0.4285` n `239`; crypto_major avg `0.7844` n `8`; equity avg `0.6727` n `168`; fx avg `-0.0131` n `6`; index avg `0.0488` n `27`; metal avg `-0.054` n `20`; unknown avg `0.489` n `1262`
- 1h: commodity avg `0.0139` n `13`; crypto_alt avg `-2.0575` n `239`; crypto_major avg `-2.4061` n `8`; equity avg `-1.265` n `168`; fx avg `-0.02` n `6`; index avg `-0.0797` n `27`; metal avg `-0.1412` n `20`; unknown avg `6.8144` n `1258`
- 4h: commodity avg `-0.3237` n `13`; crypto_alt avg `-2.1094` n `239`; crypto_major avg `-2.7906` n `8`; equity avg `-1.7983` n `168`; fx avg `-0.0306` n `6`; index avg `-0.1363` n `27`; metal avg `-0.522` n `20`; unknown avg `162.7759` n `1249`
- 24h: commodity avg `-0.2858` n `13`; crypto_alt avg `0.4436` n `239`; crypto_major avg `1.0282` n `8`; equity avg `2.0841` n `168`; fx avg `-0.1226` n `6`; index avg `0.1761` n `27`; metal avg `0.6638` n `20`; unknown avg `92.0095` n `1027`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
