# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T15:37:39.297236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0953` n `13`; crypto_alt avg `-0.7697` n `238`; crypto_major avg `-0.6498` n `8`; equity avg `-0.3294` n `156`; fx avg `0.0127` n `6`; index avg `-0.0365` n `27`; metal avg `-0.0278` n `20`; unknown avg `1.8472` n `1261`
- 1h: commodity avg `-0.0789` n `13`; crypto_alt avg `0.7798` n `238`; crypto_major avg `0.734` n `8`; equity avg `-0.4169` n `156`; fx avg `0.0064` n `6`; index avg `-0.0247` n `27`; metal avg `-0.0394` n `20`; unknown avg `2.1909` n `1255`
- 4h: commodity avg `-0.0546` n `13`; crypto_alt avg `-0.1077` n `238`; crypto_major avg `-0.5267` n `8`; equity avg `-1.2952` n `156`; fx avg `-0.0702` n `6`; index avg `-0.0712` n `27`; metal avg `-0.3075` n `20`; unknown avg `5.3889` n `1147`
- 24h: commodity avg `0.5892` n `13`; crypto_alt avg `-5.5794` n `238`; crypto_major avg `-4.605` n `8`; equity avg `-6.0568` n `156`; fx avg `-0.0768` n `6`; index avg `-0.511` n `27`; metal avg `-0.9296` n `20`; unknown avg `40.1505` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
