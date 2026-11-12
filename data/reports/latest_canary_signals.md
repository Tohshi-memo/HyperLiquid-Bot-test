# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T14:07:38.088210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0276` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6779` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0259` n `13`; crypto_alt avg `-0.094` n `239`; crypto_major avg `-0.1953` n `8`; equity avg `-0.4302` n `162`; fx avg `0.0003` n `6`; index avg `-0.0229` n `27`; metal avg `0.0086` n `20`; unknown avg `2.2199` n `1257`
- 1h: commodity avg `0.3027` n `13`; crypto_alt avg `-0.4715` n `239`; crypto_major avg `-0.6765` n `8`; equity avg `-1.0491` n `162`; fx avg `0.0128` n `6`; index avg `-0.0499` n `27`; metal avg `-0.3049` n `20`; unknown avg `-0.0303` n `1253`
- 4h: commodity avg `0.2418` n `13`; crypto_alt avg `-1.3414` n `239`; crypto_major avg `-1.7858` n `8`; equity avg `-2.0314` n `162`; fx avg `-0.0047` n `6`; index avg `-0.1079` n `27`; metal avg `-0.3527` n `20`; unknown avg `21.4552` n `1245`
- 24h: commodity avg `0.0987` n `13`; crypto_alt avg `-3.5192` n `239`; crypto_major avg `-2.9453` n `8`; equity avg `-2.88` n `162`; fx avg `-0.0661` n `6`; index avg `-0.1542` n `27`; metal avg `-1.0922` n `20`; unknown avg `0.8538` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
