# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T12:37:25.657317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.1681` n `232`; crypto_major avg `-0.1826` n `8`; equity avg `-0.1501` n `132`; fx avg `0.0128` n `6`; index avg `-0.0388` n `26`; metal avg `-0.0549` n `20`; unknown avg `0.0897` n `792`
- 1h: commodity avg `0.0447` n `12`; crypto_alt avg `0.1457` n `232`; crypto_major avg `0.1509` n `8`; equity avg `0.311` n `132`; fx avg `0.005` n `6`; index avg `0.0299` n `26`; metal avg `0.0303` n `20`; unknown avg `0.1491` n `790`
- 4h: commodity avg `-0.1192` n `12`; crypto_alt avg `-0.921` n `232`; crypto_major avg `-0.6066` n `8`; equity avg `0.0998` n `132`; fx avg `-0.0529` n `6`; index avg `0.0207` n `26`; metal avg `0.1673` n `20`; unknown avg `0.359` n `790`
- 24h: commodity avg `0.4741` n `12`; crypto_alt avg `-0.8096` n `232`; crypto_major avg `-1.7421` n `8`; equity avg `-0.7837` n `130`; fx avg `-0.2775` n `6`; index avg `-0.1126` n `26`; metal avg `-0.164` n `20`; unknown avg `-0.1518` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
