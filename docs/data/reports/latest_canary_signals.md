# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T04:48:42.045257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `0.0209` n `230`; crypto_major avg `-0.0043` n `8`; equity avg `0.0651` n `98`; fx avg `-0.0074` n `6`; index avg `0.0394` n `25`; metal avg `-0.0126` n `20`; unknown avg `-0.125` n `769`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.1799` n `230`; crypto_major avg `-0.1575` n `8`; equity avg `0.1444` n `98`; fx avg `-0.014` n `6`; index avg `0.0458` n `25`; metal avg `-0.0537` n `20`; unknown avg `0.0313` n `769`
- 4h: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.0949` n `230`; crypto_major avg `0.0615` n `8`; equity avg `0.0464` n `98`; fx avg `-0.0365` n `6`; index avg `0.0403` n `25`; metal avg `0.0702` n `20`; unknown avg `-0.2326` n `769`
- 24h: commodity avg `-0.042` n `12`; crypto_alt avg `0.0079` n `230`; crypto_major avg `0.1408` n `8`; equity avg `0.5301` n `97`; fx avg `-0.0146` n `6`; index avg `0.1343` n `25`; metal avg `0.09` n `20`; unknown avg `0.0057` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1138`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0971`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0948`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
