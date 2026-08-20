# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T22:50:11.682475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `0.0242` n `230`; crypto_major avg `0.0163` n `8`; equity avg `0.0044` n `121`; fx avg `-0.0202` n `6`; index avg `0.0202` n `25`; metal avg `0.0128` n `20`; unknown avg `0.021` n `793`
- 1h: commodity avg `0.0042` n `12`; crypto_alt avg `0.0602` n `230`; crypto_major avg `-0.3545` n `8`; equity avg `-0.0123` n `121`; fx avg `-0.0229` n `6`; index avg `0.0149` n `25`; metal avg `0.0457` n `20`; unknown avg `0.0426` n `793`
- 4h: commodity avg `-0.0819` n `12`; crypto_alt avg `0.7929` n `230`; crypto_major avg `0.3164` n `8`; equity avg `0.5159` n `121`; fx avg `-0.0398` n `6`; index avg `0.0548` n `25`; metal avg `0.0806` n `20`; unknown avg `-0.255` n `792`
- 24h: commodity avg `0.3891` n `12`; crypto_alt avg `4.5979` n `230`; crypto_major avg `5.0934` n `8`; equity avg `-1.0969` n `121`; fx avg `0.1682` n `6`; index avg `-0.1365` n `25`; metal avg `0.1305` n `20`; unknown avg `2.6933` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
