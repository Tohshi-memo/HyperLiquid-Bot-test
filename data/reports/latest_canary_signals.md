# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T22:37:30.176579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.0621` n `232`; crypto_major avg `0.0703` n `8`; equity avg `0.0348` n `132`; fx avg `-0.0012` n `6`; index avg `0.0021` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.3017` n `792`
- 1h: commodity avg `0.12` n `12`; crypto_alt avg `0.0423` n `232`; crypto_major avg `0.1092` n `8`; equity avg `-0.1078` n `132`; fx avg `0.0167` n `6`; index avg `-0.0179` n `26`; metal avg `-0.0471` n `20`; unknown avg `0.2868` n `790`
- 4h: commodity avg `0.1667` n `12`; crypto_alt avg `0.4702` n `232`; crypto_major avg `0.4952` n `8`; equity avg `0.0368` n `132`; fx avg `0.0116` n `6`; index avg `0.0304` n `26`; metal avg `-0.0277` n `20`; unknown avg `0.6301` n `772`
- 24h: commodity avg `0.9059` n `12`; crypto_alt avg `-0.6471` n `232`; crypto_major avg `-2.1322` n `8`; equity avg `-2.1667` n `130`; fx avg `0.0423` n `6`; index avg `-0.3383` n `26`; metal avg `-0.9023` n `20`; unknown avg `-0.0495` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0428`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0391`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0316`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0307`, n `668`, weak_sample_signal
