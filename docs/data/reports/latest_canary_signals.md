# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T08:07:30.119747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1024` n `12`; crypto_alt avg `-0.2577` n `232`; crypto_major avg `-0.2067` n `8`; equity avg `-0.4029` n `130`; fx avg `-0.0028` n `6`; index avg `-0.078` n `26`; metal avg `-0.0986` n `20`; unknown avg `-0.0824` n `790`
- 1h: commodity avg `0.1619` n `12`; crypto_alt avg `-0.4275` n `232`; crypto_major avg `-0.4746` n `8`; equity avg `-0.6307` n `130`; fx avg `0.0015` n `6`; index avg `-0.121` n `26`; metal avg `-0.1747` n `20`; unknown avg `0.0943` n `790`
- 4h: commodity avg `0.2242` n `12`; crypto_alt avg `-0.1344` n `232`; crypto_major avg `-0.521` n `8`; equity avg `-0.5069` n `130`; fx avg `-0.0021` n `6`; index avg `-0.0869` n `26`; metal avg `-0.1955` n `20`; unknown avg `0.2106` n `770`
- 24h: commodity avg `0.6397` n `12`; crypto_alt avg `1.204` n `232`; crypto_major avg `0.8159` n `8`; equity avg `-0.1697` n `130`; fx avg `0.0685` n `6`; index avg `-0.1371` n `26`; metal avg `-0.3996` n `20`; unknown avg `0.2849` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0419`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.041`, n `668`, weak_sample_signal
