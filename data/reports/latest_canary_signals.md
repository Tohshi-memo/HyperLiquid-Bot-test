# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T11:37:29.599237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `0.0088` n `230`; crypto_major avg `-0.0318` n `8`; equity avg `0.0001` n `96`; fx avg `0.0015` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.0002` n `770`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.005` n `230`; crypto_major avg `0.0183` n `8`; equity avg `0.0062` n `96`; fx avg `-0.0017` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0072` n `20`; unknown avg `-0.0216` n `769`
- 4h: commodity avg `0.1624` n `12`; crypto_alt avg `-0.1084` n `230`; crypto_major avg `-0.0633` n `8`; equity avg `-0.125` n `96`; fx avg `-0.002` n `6`; index avg `0.0752` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.1413` n `769`
- 24h: commodity avg `0.6933` n `12`; crypto_alt avg `-0.5397` n `230`; crypto_major avg `0.0923` n `8`; equity avg `0.5195` n `96`; fx avg `0.0102` n `6`; index avg `0.1564` n `25`; metal avg `0.2819` n `20`; unknown avg `0.0625` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
