# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T08:22:28.482026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.3605` n `232`; crypto_major avg `-0.1619` n `8`; equity avg `-0.1818` n `130`; fx avg `-0.0002` n `6`; index avg `-0.0336` n `26`; metal avg `-0.1054` n `20`; unknown avg `-0.1311` n `792`
- 1h: commodity avg `0.0615` n `12`; crypto_alt avg `-0.9124` n `232`; crypto_major avg `-0.6515` n `8`; equity avg `-0.8257` n `130`; fx avg `-0.015` n `6`; index avg `-0.1595` n `26`; metal avg `-0.3098` n `20`; unknown avg `0.0082` n `790`
- 4h: commodity avg `0.1847` n `12`; crypto_alt avg `-0.6396` n `232`; crypto_major avg `-0.7441` n `8`; equity avg `-0.7446` n `130`; fx avg `-0.0118` n `6`; index avg `-0.1268` n `26`; metal avg `-0.2869` n `20`; unknown avg `0.0117` n `770`
- 24h: commodity avg `0.5587` n `12`; crypto_alt avg `0.8715` n `232`; crypto_major avg `0.6283` n `8`; equity avg `-0.2911` n `130`; fx avg `0.0914` n `6`; index avg `-0.164` n `26`; metal avg `-0.4515` n `20`; unknown avg `0.2054` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0413`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0353`, n `668`, weak_sample_signal
