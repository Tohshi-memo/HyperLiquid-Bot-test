# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T19:37:26.024382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0811` n `12`; crypto_alt avg `-0.0975` n `230`; crypto_major avg `-0.175` n `8`; equity avg `0.0712` n `98`; fx avg `-0.0009` n `6`; index avg `0.048` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0084` n `770`
- 1h: commodity avg `-0.0781` n `12`; crypto_alt avg `-0.4454` n `230`; crypto_major avg `-0.6065` n `8`; equity avg `-0.5768` n `98`; fx avg `-0.0115` n `6`; index avg `-0.0573` n `25`; metal avg `-0.0171` n `20`; unknown avg `0.1924` n `770`
- 4h: commodity avg `0.1889` n `12`; crypto_alt avg `0.3786` n `230`; crypto_major avg `0.2838` n `8`; equity avg `-0.4961` n `98`; fx avg `-0.005` n `6`; index avg `-0.1297` n `25`; metal avg `-0.0834` n `20`; unknown avg `-0.1035` n `770`
- 24h: commodity avg `-0.33` n `12`; crypto_alt avg `1.5521` n `230`; crypto_major avg `1.0303` n `8`; equity avg `-0.0963` n `98`; fx avg `-0.1534` n `6`; index avg `0.0982` n `25`; metal avg `0.1044` n `20`; unknown avg `0.1737` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0928`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0841`, n `666`, weak_sample_signal
