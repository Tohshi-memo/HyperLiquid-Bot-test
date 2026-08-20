# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T21:07:26.951526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1455` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.0622` n `230`; crypto_major avg `0.381` n `8`; equity avg `0.0276` n `121`; fx avg `0.0106` n `6`; index avg `0.0049` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.1175` n `793`
- 1h: commodity avg `-0.0286` n `12`; crypto_alt avg `0.3886` n `230`; crypto_major avg `0.5628` n `8`; equity avg `-0.0304` n `121`; fx avg `0.0169` n `6`; index avg `0.0115` n `25`; metal avg `-0.0489` n `20`; unknown avg `-0.117` n `792`
- 4h: commodity avg `0.1367` n `12`; crypto_alt avg `-0.4084` n `230`; crypto_major avg `-1.1874` n `8`; equity avg `0.2709` n `121`; fx avg `0.0108` n `6`; index avg `-0.0419` n `25`; metal avg `0.0239` n `20`; unknown avg `-0.3164` n `792`
- 24h: commodity avg `0.3015` n `12`; crypto_alt avg `3.27` n `230`; crypto_major avg `4.6109` n `8`; equity avg `-0.8291` n `121`; fx avg `0.2335` n `6`; index avg `-0.0845` n `25`; metal avg `0.0404` n `20`; unknown avg `2.6201` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
