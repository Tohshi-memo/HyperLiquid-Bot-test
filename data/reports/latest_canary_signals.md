# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T15:52:26.919145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `0.0834` n `232`; crypto_major avg `0.1624` n `8`; equity avg `0.2043` n `131`; fx avg `-0.0004` n `6`; index avg `0.0451` n `26`; metal avg `0.0598` n `20`; unknown avg `0.1456` n `792`
- 1h: commodity avg `0.1072` n `12`; crypto_alt avg `-0.0771` n `232`; crypto_major avg `-0.1041` n `8`; equity avg `0.3154` n `131`; fx avg `-0.0164` n `6`; index avg `0.0315` n `26`; metal avg `0.1001` n `20`; unknown avg `0.3098` n `790`
- 4h: commodity avg `0.1049` n `12`; crypto_alt avg `-0.0826` n `232`; crypto_major avg `-0.3129` n `8`; equity avg `-0.0683` n `130`; fx avg `-0.0357` n `6`; index avg `0.0725` n `26`; metal avg `0.0153` n `20`; unknown avg `0.3825` n `790`
- 24h: commodity avg `0.3761` n `12`; crypto_alt avg `1.3199` n `232`; crypto_major avg `-0.188` n `8`; equity avg `-0.7108` n `130`; fx avg `0.011` n `6`; index avg `-0.08` n `26`; metal avg `-0.4102` n `20`; unknown avg `-0.0556` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0367`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0322`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0313`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0312`, n `668`, weak_sample_signal
