# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T10:37:25.843584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: crypto_alt avg `0.0164` n `225`; crypto_major avg `0.0567` n `7`; metal avg `-0.0225` n `1`; unknown avg `0.0833` n `703`
- 1h: crypto_alt avg `-0.0098` n `225`; crypto_major avg `-0.0002` n `7`; metal avg `-0.0524` n `1`; unknown avg `0.073` n `703`
- 4h: crypto_alt avg `-0.0882` n `225`; crypto_major avg `-0.0018` n `7`; metal avg `-0.1047` n `1`; unknown avg `-0.0356` n `703`
- 24h: crypto_alt avg `0.3857` n `225`; crypto_major avg `1.2383` n `7`; metal avg `-0.157` n `1`; unknown avg `0.0855` n `685`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
