# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T21:52:27.129062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1205` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `0.0558` n `230`; crypto_major avg `-0.0768` n `8`; equity avg `-0.0401` n `121`; fx avg `0.0128` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0096` n `20`; unknown avg `0.0404` n `793`
- 1h: commodity avg `-0.0127` n `12`; crypto_alt avg `0.3913` n `230`; crypto_major avg `0.6052` n `8`; equity avg `0.0847` n `121`; fx avg `0.0001` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.1234` n `793`
- 4h: commodity avg `0.0404` n `12`; crypto_alt avg `-0.2042` n `230`; crypto_major avg `-1.1438` n `8`; equity avg `0.293` n `121`; fx avg `-0.0073` n `6`; index avg `-0.0233` n `25`; metal avg `0.0173` n `20`; unknown avg `-0.3024` n `792`
- 24h: commodity avg `0.3061` n `12`; crypto_alt avg `3.5212` n `230`; crypto_major avg `3.9327` n `8`; equity avg `-0.8937` n `121`; fx avg `0.2072` n `6`; index avg `-0.101` n `25`; metal avg `0.0403` n `20`; unknown avg `2.679` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
