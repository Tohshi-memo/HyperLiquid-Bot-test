# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T14:37:26.191829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: crypto_alt avg `-0.115` n `227`; crypto_major avg `-0.1748` n `7`; metal avg `0.1153` n `1`; unknown avg `0.5426` n `1013`
- 1h: crypto_alt avg `-0.5488` n `227`; crypto_major avg `-0.1368` n `7`; metal avg `-0.0192` n `1`; unknown avg `1.4632` n `1011`
- 4h: crypto_alt avg `-1.7564` n `227`; crypto_major avg `-1.5018` n `7`; metal avg `-0.1963` n `1`; unknown avg `0.2422` n `988`
- 24h: crypto_alt avg `-0.8347` n `227`; crypto_major avg `-0.4297` n `7`; metal avg `-0.5654` n `1`; unknown avg `-0.0447` n `812`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0361`, n `668`, weak_sample_signal
