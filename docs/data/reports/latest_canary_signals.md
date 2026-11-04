# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T00:52:34.497952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0444` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0046` n `13`; crypto_alt avg `0.3669` n `239`; crypto_major avg `0.355` n `8`; equity avg `0.3565` n `158`; fx avg `0.005` n `6`; index avg `0.0619` n `27`; metal avg `0.0747` n `20`; unknown avg `0.1754` n `1264`
- 1h: commodity avg `-0.0103` n `13`; crypto_alt avg `-1.0734` n `239`; crypto_major avg `-0.9917` n `8`; equity avg `-0.9968` n `158`; fx avg `0.0269` n `6`; index avg `-0.1427` n `27`; metal avg `-0.0651` n `20`; unknown avg `1.0361` n `1252`
- 4h: commodity avg `-0.0063` n `13`; crypto_alt avg `-0.7692` n `239`; crypto_major avg `-1.0976` n `8`; equity avg `-0.288` n `158`; fx avg `0.0347` n `6`; index avg `-0.0532` n `27`; metal avg `0.0232` n `20`; unknown avg `0.8276` n `1187`
- 24h: commodity avg `0.2859` n `13`; crypto_alt avg `0.1671` n `239`; crypto_major avg `0.0019` n `8`; equity avg `1.2488` n `158`; fx avg `0.1629` n `6`; index avg `0.08` n `27`; metal avg `-0.5906` n `20`; unknown avg `-0.1613` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
