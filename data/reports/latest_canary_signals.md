# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T05:37:25.210268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `0.301` n `232`; crypto_major avg `0.3186` n `8`; equity avg `0.1683` n `130`; fx avg `-0.0238` n `6`; index avg `0.0548` n `26`; metal avg `0.0907` n `20`; unknown avg `0.0507` n `792`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.2427` n `232`; crypto_major avg `0.2494` n `8`; equity avg `0.0009` n `130`; fx avg `-0.0367` n `6`; index avg `0.0301` n `26`; metal avg `0.0524` n `20`; unknown avg `-0.4089` n `790`
- 4h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.6413` n `232`; crypto_major avg `0.5887` n `8`; equity avg `0.143` n `130`; fx avg `-0.0296` n `6`; index avg `0.032` n `26`; metal avg `-0.0451` n `20`; unknown avg `-0.1388` n `790`
- 24h: commodity avg `0.2428` n `12`; crypto_alt avg `1.918` n `232`; crypto_major avg `1.7532` n `8`; equity avg `0.8849` n `130`; fx avg `-0.0301` n `6`; index avg `0.0747` n `26`; metal avg `-0.0702` n `20`; unknown avg `0.4363` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
