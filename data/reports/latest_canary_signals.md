# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T03:07:28.249222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7523` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.6786` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5135` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1099` n `13`; crypto_alt avg `-0.7827` n `239`; crypto_major avg `-0.7034` n `8`; equity avg `-0.4587` n `166`; fx avg `-0.0047` n `6`; index avg `-0.0456` n `27`; metal avg `-0.032` n `20`; unknown avg `158.8709` n `1256`
- 1h: commodity avg `0.0383` n `13`; crypto_alt avg `-1.4804` n `239`; crypto_major avg `-1.7008` n `8`; equity avg `-0.6161` n `166`; fx avg `-0.035` n `6`; index avg `-0.0222` n `27`; metal avg `-0.1873` n `20`; unknown avg `330.0284` n `1262`
- 4h: commodity avg `0.0215` n `13`; crypto_alt avg `-0.9046` n `239`; crypto_major avg `-1.748` n `8`; equity avg `-1.1446` n `166`; fx avg `0.0198` n `6`; index avg `0.0043` n `27`; metal avg `-0.2672` n `20`; unknown avg `0.6865` n `1250`
- 24h: commodity avg `-1.0746` n `13`; crypto_alt avg `0.1834` n `239`; crypto_major avg `-0.3658` n `8`; equity avg `5.0474` n `166`; fx avg `-0.2473` n `6`; index avg `0.6719` n `27`; metal avg `0.2521` n `20`; unknown avg `639.6609` n `1054`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
