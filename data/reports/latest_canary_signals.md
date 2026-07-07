# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T14:37:34.364462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0783` n `12`; crypto_alt avg `-0.478` n `229`; crypto_major avg `-0.2845` n `8`; equity avg `-0.3072` n `91`; fx avg `0.0099` n `6`; index avg `-0.0499` n `25`; metal avg `-0.0922` n `20`; unknown avg `-0.0291` n `763`
- 1h: commodity avg `0.2816` n `12`; crypto_alt avg `-0.8701` n `229`; crypto_major avg `-0.4307` n `8`; equity avg `-1.7162` n `91`; fx avg `-0.0034` n `6`; index avg `-0.2276` n `25`; metal avg `-0.3251` n `20`; unknown avg `0.0859` n `763`
- 4h: commodity avg `0.2953` n `12`; crypto_alt avg `-1.3278` n `229`; crypto_major avg `-0.7141` n `8`; equity avg `-2.1719` n `91`; fx avg `-0.012` n `6`; index avg `-0.2596` n `25`; metal avg `-0.0558` n `20`; unknown avg `-0.0255` n `763`
- 24h: commodity avg `0.4353` n `12`; crypto_alt avg `-0.426` n `229`; crypto_major avg `0.2277` n `8`; equity avg `-4.0255` n `90`; fx avg `-0.175` n `6`; index avg `-0.7335` n `25`; metal avg `-0.1162` n `20`; unknown avg `0.0591` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
