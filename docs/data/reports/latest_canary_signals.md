# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T02:52:32.298883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0547` n `12`; crypto_alt avg `-0.0521` n `228`; crypto_major avg `0.0025` n `8`; equity avg `-0.001` n `88`; fx avg `-0.0031` n `6`; index avg `-0.003` n `23`; metal avg `0.002` n `20`; unknown avg `1.4369` n `730`
- 1h: commodity avg `-0.055` n `12`; crypto_alt avg `-0.151` n `228`; crypto_major avg `-0.1457` n `8`; equity avg `-0.0197` n `88`; fx avg `-0.0047` n `6`; index avg `-0.0098` n `23`; metal avg `-0.0034` n `20`; unknown avg `15.5941` n `722`
- 4h: commodity avg `0.3117` n `12`; crypto_alt avg `-0.0545` n `228`; crypto_major avg `-0.3878` n `8`; equity avg `-0.1282` n `88`; fx avg `-0.0423` n `6`; index avg `-0.0498` n `23`; metal avg `0.0263` n `20`; unknown avg `15.3726` n `722`
- 24h: commodity avg `0.4662` n `12`; crypto_alt avg `-1.258` n `228`; crypto_major avg `-1.5971` n `8`; equity avg `0.0116` n `88`; fx avg `-0.0182` n `6`; index avg `-0.1357` n `23`; metal avg `-0.0516` n `20`; unknown avg `5.996` n `674`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2165`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
