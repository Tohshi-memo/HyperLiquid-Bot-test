# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T05:56:04.831121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0338` n `12`; crypto_alt avg `-0.1633` n `230`; crypto_major avg `-0.1457` n `8`; equity avg `-0.085` n `121`; fx avg `-0.0132` n `6`; index avg `-0.0241` n `25`; metal avg `-0.0099` n `20`; unknown avg `5.3639` n `792`
- 1h: commodity avg `0.05` n `12`; crypto_alt avg `-0.1005` n `230`; crypto_major avg `0.0072` n `8`; equity avg `-0.2093` n `121`; fx avg `0.0117` n `6`; index avg `-0.0467` n `25`; metal avg `-0.1163` n `20`; unknown avg `-0.1531` n `792`
- 4h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.3634` n `230`; crypto_major avg `-0.2212` n `8`; equity avg `-0.2537` n `121`; fx avg `0.0254` n `6`; index avg `-0.061` n `25`; metal avg `-0.0275` n `20`; unknown avg `-0.1069` n `792`
- 24h: commodity avg `-0.0458` n `12`; crypto_alt avg `5.3592` n `230`; crypto_major avg `9.8597` n `8`; equity avg `1.3801` n `120`; fx avg `0.1033` n `6`; index avg `0.3273` n `25`; metal avg `1.0362` n `20`; unknown avg `1.7154` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
