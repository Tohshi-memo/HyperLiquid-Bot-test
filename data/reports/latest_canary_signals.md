# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T01:07:25.174972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `-0.1593` n `232`; crypto_major avg `-0.077` n `8`; equity avg `-0.0141` n `132`; fx avg `0.0162` n `6`; index avg `0.0006` n `26`; metal avg `-0.0327` n `20`; unknown avg `-0.346` n `790`
- 1h: commodity avg `0.1007` n `12`; crypto_alt avg `-0.4784` n `232`; crypto_major avg `-0.3648` n `8`; equity avg `0.0472` n `132`; fx avg `-0.0048` n `6`; index avg `0.0021` n `26`; metal avg `-0.0656` n `20`; unknown avg `2.215` n `790`
- 4h: commodity avg `0.2436` n `12`; crypto_alt avg `-0.2691` n `232`; crypto_major avg `-0.0481` n `8`; equity avg `-0.1619` n `132`; fx avg `-0.0312` n `6`; index avg `0.0021` n `26`; metal avg `-0.119` n `20`; unknown avg `0.1579` n `784`
- 24h: commodity avg `1.0264` n `12`; crypto_alt avg `-1.2757` n `232`; crypto_major avg `-2.0229` n `8`; equity avg `-2.1613` n `130`; fx avg `-0.0213` n `6`; index avg `-0.383` n `26`; metal avg `-1.0845` n `20`; unknown avg `0.0804` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0399`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0313`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.031`, n `668`, weak_sample_signal
