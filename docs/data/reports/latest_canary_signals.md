# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T21:37:00.475170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.0095` n `230`; crypto_major avg `-0.0072` n `8`; equity avg `0.0775` n `98`; fx avg `-0.0062` n `6`; index avg `0.0027` n `25`; metal avg `0.0055` n `20`; unknown avg `1.8473` n `770`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `0.0789` n `230`; crypto_major avg `0.073` n `8`; equity avg `0.1636` n `98`; fx avg `-0.0048` n `6`; index avg `0.0027` n `25`; metal avg `0.0054` n `20`; unknown avg `0.4494` n `770`
- 4h: commodity avg `0.0167` n `12`; crypto_alt avg `0.3843` n `230`; crypto_major avg `0.2496` n `8`; equity avg `-0.645` n `98`; fx avg `-0.01` n `6`; index avg `-0.1341` n `25`; metal avg `-0.077` n `20`; unknown avg `0.0915` n `770`
- 24h: commodity avg `-0.4021` n `12`; crypto_alt avg `1.9318` n `230`; crypto_major avg `1.5409` n `8`; equity avg `-0.2412` n `98`; fx avg `-0.2285` n `6`; index avg `0.0091` n `25`; metal avg `0.1417` n `20`; unknown avg `0.3312` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
