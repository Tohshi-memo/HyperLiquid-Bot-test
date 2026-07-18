# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T12:37:25.309483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.1403` n `230`; crypto_major avg `0.1113` n `8`; equity avg `-0.046` n `96`; fx avg `0.0019` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0095` n `20`; unknown avg `0.0037` n `770`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `-0.0304` n `230`; crypto_major avg `0.0025` n `8`; equity avg `-0.0897` n `96`; fx avg `0.0008` n `6`; index avg `-0.029` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.0225` n `770`
- 4h: commodity avg `0.1384` n `12`; crypto_alt avg `-0.208` n `230`; crypto_major avg `-0.1364` n `8`; equity avg `-0.1801` n `96`; fx avg `0.0047` n `6`; index avg `0.0006` n `25`; metal avg `-0.016` n `20`; unknown avg `-0.0657` n `769`
- 24h: commodity avg `0.5893` n `12`; crypto_alt avg `-0.3717` n `230`; crypto_major avg `0.4071` n `8`; equity avg `0.9865` n `96`; fx avg `0.0406` n `6`; index avg `0.192` n `25`; metal avg `0.3691` n `20`; unknown avg `0.0193` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
