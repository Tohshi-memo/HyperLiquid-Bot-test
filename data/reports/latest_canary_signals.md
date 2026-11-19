# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T16:07:47.921669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3946` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1354` n `13`; crypto_alt avg `-0.0023` n `239`; crypto_major avg `0.1305` n `8`; equity avg `0.4225` n `165`; fx avg `-0.0171` n `6`; index avg `0.0508` n `27`; metal avg `-0.0539` n `20`; unknown avg `4.2253` n `1253`
- 1h: commodity avg `-0.0892` n `13`; crypto_alt avg `-1.4335` n `239`; crypto_major avg `-1.6291` n `8`; equity avg `-1.8924` n `165`; fx avg `0.0128` n `6`; index avg `-0.2345` n `27`; metal avg `-0.4266` n `20`; unknown avg `14.3259` n `1257`
- 4h: commodity avg `0.0856` n `13`; crypto_alt avg `-1.4293` n `239`; crypto_major avg `-1.2351` n `8`; equity avg `-1.7254` n `165`; fx avg `-0.009` n `6`; index avg `-0.2816` n `27`; metal avg `-0.4236` n `20`; unknown avg `1.3093` n `1255`
- 24h: commodity avg `0.236` n `13`; crypto_alt avg `0.0119` n `239`; crypto_major avg `0.4605` n `8`; equity avg `1.0439` n `165`; fx avg `0.047` n `6`; index avg `0.1846` n `27`; metal avg `-0.4606` n `20`; unknown avg `3.1884` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
