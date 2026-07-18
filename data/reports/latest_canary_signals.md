# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T16:22:24.482709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `-0.0506` n `230`; crypto_major avg `0.0714` n `8`; equity avg `0.0053` n `96`; fx avg `0.0008` n `6`; index avg `-0.0062` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0124` n `770`
- 1h: commodity avg `0.0033` n `12`; crypto_alt avg `-0.1588` n `230`; crypto_major avg `-0.0087` n `8`; equity avg `-0.0942` n `96`; fx avg `-0.0388` n `6`; index avg `-0.0116` n `25`; metal avg `-0.0182` n `20`; unknown avg `-0.0692` n `770`
- 4h: commodity avg `0.0164` n `12`; crypto_alt avg `0.0828` n `230`; crypto_major avg `0.2221` n `8`; equity avg `-0.1468` n `96`; fx avg `-0.0429` n `6`; index avg `-0.0256` n `25`; metal avg `-0.0509` n `20`; unknown avg `-0.0903` n `770`
- 24h: commodity avg `0.3606` n `12`; crypto_alt avg `-0.7933` n `230`; crypto_major avg `0.2913` n `8`; equity avg `-0.8667` n `96`; fx avg `-0.0964` n `6`; index avg `-0.0439` n `25`; metal avg `-0.0279` n `20`; unknown avg `0.0604` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
