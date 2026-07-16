# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T03:07:29.912882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.0574` n `230`; crypto_major avg `0.0647` n `8`; equity avg `0.0708` n `94`; fx avg `-0.0027` n `6`; index avg `0.0251` n `25`; metal avg `0.0611` n `20`; unknown avg `0.1517` n `768`
- 1h: commodity avg `-0.0223` n `12`; crypto_alt avg `0.094` n `230`; crypto_major avg `0.0546` n `8`; equity avg `0.3636` n `94`; fx avg `-0.0256` n `6`; index avg `0.132` n `25`; metal avg `0.0622` n `20`; unknown avg `-0.1444` n `768`
- 4h: commodity avg `-0.0974` n `12`; crypto_alt avg `0.0645` n `230`; crypto_major avg `-0.2831` n `8`; equity avg `-0.1764` n `94`; fx avg `-0.0248` n `6`; index avg `-0.0654` n `25`; metal avg `-0.1865` n `20`; unknown avg `-0.3014` n `766`
- 24h: commodity avg `-0.0803` n `12`; crypto_alt avg `0.5793` n `230`; crypto_major avg `0.426` n `8`; equity avg `-2.0065` n `93`; fx avg `0.1225` n `6`; index avg `-0.3888` n `25`; metal avg `-0.0412` n `20`; unknown avg `0.0343` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
