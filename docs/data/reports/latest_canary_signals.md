# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T15:22:28.836248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0413` n `13`; crypto_alt avg `0.0006` n `236`; crypto_major avg `-0.0679` n `8`; equity avg `-0.0802` n `151`; fx avg `0.0121` n `6`; index avg `-0.0058` n `26`; metal avg `-0.001` n `20`; unknown avg `1.5551` n `1193`
- 1h: commodity avg `0.0662` n `13`; crypto_alt avg `-0.3147` n `236`; crypto_major avg `-0.0923` n `8`; equity avg `-0.1456` n `151`; fx avg `0.0114` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0005` n `20`; unknown avg `1.9975` n `1173`
- 4h: commodity avg `0.0923` n `13`; crypto_alt avg `-0.9101` n `236`; crypto_major avg `-0.3915` n `8`; equity avg `-0.2596` n `151`; fx avg `0.005` n `6`; index avg `-0.0609` n `26`; metal avg `-0.0229` n `20`; unknown avg `5.193` n `1167`
- 24h: commodity avg `0.7821` n `13`; crypto_alt avg `-1.6236` n `236`; crypto_major avg `-0.3343` n `8`; equity avg `-1.4144` n `151`; fx avg `0.0033` n `6`; index avg `-0.2755` n `26`; metal avg `-0.1539` n `20`; unknown avg `0.862` n `1030`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1726`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1449`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.113`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0705`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
