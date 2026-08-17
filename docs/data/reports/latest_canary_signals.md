# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T13:37:32.347234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `12`; crypto_alt avg `0.2243` n `230`; crypto_major avg `0.3772` n `8`; equity avg `0.091` n `114`; fx avg `0.0051` n `6`; index avg `0.0076` n `25`; metal avg `0.0256` n `20`; unknown avg `0.0409` n `792`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `0.1482` n `230`; crypto_major avg `0.2371` n `8`; equity avg `0.1189` n `114`; fx avg `0.0235` n `6`; index avg `0.018` n `25`; metal avg `-0.0134` n `20`; unknown avg `0.007` n `792`
- 4h: commodity avg `0.0735` n `12`; crypto_alt avg `0.33` n `230`; crypto_major avg `0.3087` n `8`; equity avg `-0.2452` n `114`; fx avg `0.0376` n `6`; index avg `-0.0104` n `25`; metal avg `-0.0761` n `20`; unknown avg `1.5279` n `792`
- 24h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.0146` n `230`; crypto_major avg `0.8566` n `8`; equity avg `1.0149` n `114`; fx avg `0.0228` n `6`; index avg `0.1105` n `25`; metal avg `0.079` n `20`; unknown avg `0.0903` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
