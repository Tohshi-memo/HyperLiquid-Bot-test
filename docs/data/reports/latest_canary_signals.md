# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T12:07:27.668041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1099` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `0.1291` n `230`; crypto_major avg `0.0731` n `8`; equity avg `-0.0372` n `121`; fx avg `0.0266` n `6`; index avg `-0.0101` n `23`; metal avg `0.004` n `18`; unknown avg `-0.0275` n `774`
- 1h: commodity avg `-0.1033` n `12`; crypto_alt avg `0.0101` n `230`; crypto_major avg `-1.0857` n `8`; equity avg `0.0506` n `121`; fx avg `0.0036` n `6`; index avg `0.0242` n `25`; metal avg `0.046` n `20`; unknown avg `0.1591` n `793`
- 4h: commodity avg `-0.009` n `12`; crypto_alt avg `1.5188` n `230`; crypto_major avg `0.2994` n `8`; equity avg `0.2012` n `121`; fx avg `0.0362` n `6`; index avg `0.0051` n `25`; metal avg `0.1516` n `20`; unknown avg `0.5684` n `793`
- 24h: commodity avg `0.0291` n `12`; crypto_alt avg `7.4893` n `230`; crypto_major avg `6.1069` n `8`; equity avg `1.5819` n `121`; fx avg `-0.0827` n `6`; index avg `0.2325` n `25`; metal avg `1.1935` n `20`; unknown avg `2.4286` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
