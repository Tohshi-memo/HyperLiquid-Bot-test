# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T18:33:08.305887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.0034` n `230`; crypto_major avg `0.019` n `8`; equity avg `0.0045` n `96`; fx avg `-0.0014` n `6`; index avg `-0.0023` n `25`; metal avg `0.0165` n `20`; unknown avg `0.0749` n `770`
- 1h: commodity avg `0.13` n `12`; crypto_alt avg `0.0237` n `230`; crypto_major avg `0.1565` n `8`; equity avg `0.0216` n `96`; fx avg `-0.018` n `6`; index avg `-0.0118` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.1403` n `770`
- 4h: commodity avg `0.2133` n `12`; crypto_alt avg `0.2625` n `230`; crypto_major avg `0.367` n `8`; equity avg `-0.0222` n `96`; fx avg `-0.074` n `6`; index avg `-0.026` n `25`; metal avg `-0.0277` n `20`; unknown avg `0.1139` n `770`
- 24h: commodity avg `0.3927` n `12`; crypto_alt avg `-0.6745` n `230`; crypto_major avg `0.3345` n `8`; equity avg `-0.7907` n `96`; fx avg `-0.1355` n `6`; index avg `-0.0613` n `25`; metal avg `-0.0246` n `20`; unknown avg `-0.0559` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
