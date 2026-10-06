# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T01:37:34.293864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `13`; crypto_alt avg `-0.1166` n `235`; crypto_major avg `-0.1471` n `8`; equity avg `-0.058` n `144`; fx avg `-0.0006` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0172` n `20`; unknown avg `0.6138` n `1079`
- 1h: commodity avg `0.0025` n `13`; crypto_alt avg `-0.4381` n `235`; crypto_major avg `-0.1108` n `8`; equity avg `-0.1959` n `144`; fx avg `0.0514` n `6`; index avg `-0.0368` n `26`; metal avg `-0.014` n `20`; unknown avg `-0.0558` n `1077`
- 4h: commodity avg `0.0615` n `13`; crypto_alt avg `-0.8352` n `235`; crypto_major avg `-0.1942` n `8`; equity avg `-0.09` n `144`; fx avg `0.0536` n `6`; index avg `-0.0512` n `26`; metal avg `-0.021` n `20`; unknown avg `0.2745` n `1047`
- 24h: commodity avg `-0.0626` n `13`; crypto_alt avg `-0.3929` n `235`; crypto_major avg `-0.1384` n `8`; equity avg `-0.2103` n `144`; fx avg `0.0371` n `6`; index avg `0.0319` n `26`; metal avg `-0.0383` n `20`; unknown avg `625.3442` n `800`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
