# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T14:37:30.366659+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `1.1414` n `231`; crypto_major avg `1.2106` n `8`; equity avg `0.2268` n `127`; fx avg `0.0024` n `6`; index avg `0.0445` n `26`; metal avg `0.1451` n `20`; unknown avg `0.2905` n `793`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `0.801` n `231`; crypto_major avg `0.7712` n `8`; equity avg `0.2185` n `127`; fx avg `-0.0265` n `6`; index avg `0.0649` n `26`; metal avg `-0.1352` n `20`; unknown avg `0.1239` n `793`
- 4h: commodity avg `-0.1841` n `12`; crypto_alt avg `0.6216` n `231`; crypto_major avg `0.8021` n `8`; equity avg `0.023` n `127`; fx avg `-0.0257` n `6`; index avg `0.081` n `26`; metal avg `-0.0104` n `20`; unknown avg `0.0016` n `792`
- 24h: commodity avg `-0.1581` n `12`; crypto_alt avg `-0.9014` n `231`; crypto_major avg `-0.5242` n `8`; equity avg `-0.7538` n `127`; fx avg `-0.1029` n `6`; index avg `0.098` n `26`; metal avg `0.6635` n `20`; unknown avg `0.2955` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
