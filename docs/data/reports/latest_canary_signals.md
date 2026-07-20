# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T19:22:30.101892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0237` n `12`; crypto_alt avg `-0.1058` n `230`; crypto_major avg `-0.0924` n `8`; equity avg `-0.1545` n `98`; fx avg `-0.0045` n `6`; index avg `-0.0292` n `25`; metal avg `0.0201` n `20`; unknown avg `0.0062` n `770`
- 1h: commodity avg `0.0745` n `12`; crypto_alt avg `-0.3513` n `230`; crypto_major avg `-0.4944` n `8`; equity avg `-0.8056` n `98`; fx avg `-0.0154` n `6`; index avg `-0.1492` n `25`; metal avg `-0.037` n `20`; unknown avg `0.4786` n `770`
- 4h: commodity avg `0.2467` n `12`; crypto_alt avg `0.424` n `230`; crypto_major avg `0.4115` n `8`; equity avg `-0.5193` n `98`; fx avg `-0.0016` n `6`; index avg `-0.1406` n `25`; metal avg `-0.0725` n `20`; unknown avg `-0.0864` n `770`
- 24h: commodity avg `-0.2665` n `12`; crypto_alt avg `1.662` n `230`; crypto_major avg `1.2604` n `8`; equity avg `-0.143` n `98`; fx avg `-0.1519` n `6`; index avg `0.0639` n `25`; metal avg `0.1142` n `20`; unknown avg `0.2158` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1051`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0922`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `666`, weak_sample_signal
