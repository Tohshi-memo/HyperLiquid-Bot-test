# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T13:37:37.705984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.0092` n `232`; crypto_major avg `-0.1451` n `8`; equity avg `-0.3267` n `131`; fx avg `-0.0018` n `6`; index avg `0.0109` n `26`; metal avg `0.1322` n `20`; unknown avg `0.4109` n `792`
- 1h: commodity avg `0.012` n `12`; crypto_alt avg `0.1013` n `232`; crypto_major avg `-0.0342` n `8`; equity avg `-0.2565` n `130`; fx avg `-0.0193` n `6`; index avg `0.016` n `26`; metal avg `-0.0102` n `20`; unknown avg `0.3129` n `790`
- 4h: commodity avg `-0.0832` n `12`; crypto_alt avg `0.2994` n `232`; crypto_major avg `-0.1971` n `8`; equity avg `-0.635` n `130`; fx avg `-0.0158` n `6`; index avg `-0.0278` n `26`; metal avg `0.0025` n `20`; unknown avg `-0.1218` n `790`
- 24h: commodity avg `0.2158` n `12`; crypto_alt avg `1.0781` n `232`; crypto_major avg `0.0858` n `8`; equity avg `-1.3675` n `130`; fx avg `0.0637` n `6`; index avg `-0.273` n `26`; metal avg `-0.6743` n `20`; unknown avg `0.2189` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0388`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0312`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0304`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0303`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0293`, n `668`, weak_sample_signal
