# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T13:07:25.280716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0565` n `12`; crypto_alt avg `0.0068` n `230`; crypto_major avg `0.1433` n `8`; equity avg `-0.0001` n `98`; fx avg `0.0022` n `6`; index avg `0.0023` n `25`; metal avg `0.01` n `20`; unknown avg `-0.0073` n `771`
- 1h: commodity avg `0.1453` n `12`; crypto_alt avg `0.0146` n `230`; crypto_major avg `0.2169` n `8`; equity avg `-0.0074` n `98`; fx avg `-0.0049` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0318` n `20`; unknown avg `0.0419` n `771`
- 4h: commodity avg `0.4016` n `12`; crypto_alt avg `0.134` n `230`; crypto_major avg `0.3141` n `8`; equity avg `-0.1655` n `98`; fx avg `-0.0032` n `6`; index avg `0.0024` n `25`; metal avg `-0.0752` n `20`; unknown avg `0.0636` n `771`
- 24h: commodity avg `0.4792` n `12`; crypto_alt avg `1.8808` n `230`; crypto_major avg `2.2958` n `8`; equity avg `1.1357` n `98`; fx avg `-0.066` n `6`; index avg `0.1797` n `25`; metal avg `0.6527` n `20`; unknown avg `0.1383` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0884`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0616`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0613`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
