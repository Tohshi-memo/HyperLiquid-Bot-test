# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T15:22:29.840313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0548` n `12`; crypto_alt avg `0.024` n `232`; crypto_major avg `0.1253` n `8`; equity avg `-0.0712` n `131`; fx avg `-0.0062` n `6`; index avg `0.002` n `26`; metal avg `0.0272` n `20`; unknown avg `2.0764` n `792`
- 1h: commodity avg `0.1863` n `12`; crypto_alt avg `-0.4115` n `232`; crypto_major avg `-0.4363` n `8`; equity avg `0.0613` n `131`; fx avg `-0.0086` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0823` n `20`; unknown avg `0.1859` n `790`
- 4h: commodity avg `0.0758` n `12`; crypto_alt avg `-0.0374` n `232`; crypto_major avg `-0.3668` n `8`; equity avg `-0.4486` n `130`; fx avg `-0.0312` n `6`; index avg `0.0064` n `26`; metal avg `0.0061` n `20`; unknown avg `0.0506` n `790`
- 24h: commodity avg `0.3893` n `12`; crypto_alt avg `0.9679` n `232`; crypto_major avg `-0.2536` n `8`; equity avg `-1.1565` n `130`; fx avg `0.0209` n `6`; index avg `-0.168` n `26`; metal avg `-0.5413` n `20`; unknown avg `-0.1113` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0346`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0332`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0324`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0316`, n `668`, weak_sample_signal
