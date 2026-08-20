# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T04:03:24.960597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.0814` n `230`; crypto_major avg `-0.0599` n `8`; equity avg `-0.0299` n `121`; fx avg `0.0123` n `6`; index avg `-0.0023` n `25`; metal avg `-0.014` n `20`; unknown avg `0.472` n `792`
- 1h: commodity avg `0.013` n `12`; crypto_alt avg `0.0008` n `230`; crypto_major avg `0.1043` n `8`; equity avg `0.0491` n `121`; fx avg `-0.0001` n `6`; index avg `0.0007` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.098` n `792`
- 4h: commodity avg `0.0419` n `12`; crypto_alt avg `-0.2433` n `230`; crypto_major avg `-0.4245` n `8`; equity avg `0.4505` n `121`; fx avg `0.1078` n `6`; index avg `0.1842` n `25`; metal avg `-0.1044` n `20`; unknown avg `-0.0266` n `792`
- 24h: commodity avg `-0.066` n `12`; crypto_alt avg `5.0896` n `230`; crypto_major avg `9.3542` n `8`; equity avg `1.2453` n `120`; fx avg `0.0615` n `6`; index avg `0.33` n `25`; metal avg `1.0592` n `20`; unknown avg `1.6477` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
