# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T12:22:24.716070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.358` n `230`; crypto_major avg `-0.2787` n `8`; equity avg `-0.0671` n `96`; fx avg `0.0` n `6`; index avg `-0.0018` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0191` n `770`
- 1h: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.1614` n `230`; crypto_major avg `-0.1404` n `8`; equity avg `-0.0434` n `96`; fx avg `0.0005` n `6`; index avg `-0.0223` n `25`; metal avg `-0.004` n `20`; unknown avg `0.0218` n `770`
- 4h: commodity avg `0.1258` n `12`; crypto_alt avg `-0.3551` n `230`; crypto_major avg `-0.2525` n `8`; equity avg `-0.1294` n `96`; fx avg `-0.0095` n `6`; index avg `0.0388` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.0644` n `769`
- 24h: commodity avg `0.721` n `12`; crypto_alt avg `-0.5811` n `230`; crypto_major avg `0.1595` n `8`; equity avg `0.8482` n `96`; fx avg `0.0319` n `6`; index avg `0.1933` n `25`; metal avg `0.3549` n `20`; unknown avg `0.0325` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
