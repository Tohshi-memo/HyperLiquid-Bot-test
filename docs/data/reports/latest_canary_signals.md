# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T22:52:24.791668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.1661` n `232`; crypto_major avg `0.1541` n `8`; equity avg `0.0177` n `132`; fx avg `0.0003` n `6`; index avg `0.0037` n `26`; metal avg `0.0132` n `20`; unknown avg `0.1259` n `792`
- 1h: commodity avg `0.0827` n `12`; crypto_alt avg `-0.0623` n `232`; crypto_major avg `-0.0363` n `8`; equity avg `-0.0693` n `132`; fx avg `0.0199` n `6`; index avg `-0.0149` n `26`; metal avg `-0.0621` n `20`; unknown avg `0.2609` n `790`
- 4h: commodity avg `0.1396` n `12`; crypto_alt avg `0.214` n `232`; crypto_major avg `0.2305` n `8`; equity avg `0.0873` n `132`; fx avg `0.0164` n `6`; index avg `0.0576` n `26`; metal avg `-0.023` n `20`; unknown avg `0.6807` n `772`
- 24h: commodity avg `0.9171` n `12`; crypto_alt avg `-0.5049` n `232`; crypto_major avg `-1.9135` n `8`; equity avg `-2.1199` n `130`; fx avg `0.0451` n `6`; index avg `-0.332` n `26`; metal avg `-0.8777` n `20`; unknown avg `-0.0868` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0438`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.039`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0328`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0307`, n `668`, weak_sample_signal
