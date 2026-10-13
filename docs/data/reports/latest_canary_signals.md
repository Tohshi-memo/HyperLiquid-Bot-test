# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T11:52:33.492999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1854` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0934` n `13`; crypto_alt avg `-0.1772` n `235`; crypto_major avg `-0.1534` n `8`; equity avg `0.0216` n `151`; fx avg `0.0079` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0234` n `20`; unknown avg `1.1694` n `1135`
- 1h: commodity avg `0.2167` n `13`; crypto_alt avg `-0.5631` n `235`; crypto_major avg `-0.0419` n `8`; equity avg `-0.65` n `151`; fx avg `0.0097` n `6`; index avg `-0.0199` n `26`; metal avg `0.0045` n `20`; unknown avg `0.6942` n `1133`
- 4h: commodity avg `0.1306` n `13`; crypto_alt avg `-2.2191` n `235`; crypto_major avg `-1.2342` n `8`; equity avg `-0.2244` n `151`; fx avg `-0.0268` n `6`; index avg `-0.0488` n `26`; metal avg `-0.0616` n `20`; unknown avg `0.0593` n `1117`
- 24h: commodity avg `0.0415` n `13`; crypto_alt avg `-4.4429` n `235`; crypto_major avg `-2.3319` n `8`; equity avg `-2.9879` n `151`; fx avg `0.0769` n `6`; index avg `-0.3682` n `26`; metal avg `-0.0376` n `20`; unknown avg `0.0922` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1699`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.167`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1515`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1445`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0803`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
