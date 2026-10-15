# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T14:22:27.578463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `13`; crypto_alt avg `0.717` n `236`; crypto_major avg `0.6778` n `8`; equity avg `0.2455` n `151`; fx avg `-0.0183` n `6`; index avg `0.0243` n `26`; metal avg `0.0043` n `20`; unknown avg `0.5672` n `1128`
- 1h: commodity avg `0.1033` n `13`; crypto_alt avg `1.1551` n `236`; crypto_major avg `0.8953` n `8`; equity avg `0.1921` n `151`; fx avg `0.0421` n `6`; index avg `0.1016` n `26`; metal avg `-0.0512` n `20`; unknown avg `1.5773` n `1092`
- 4h: commodity avg `0.1363` n `13`; crypto_alt avg `0.679` n `236`; crypto_major avg `0.1482` n `8`; equity avg `-0.3975` n `151`; fx avg `0.0529` n `6`; index avg `0.0632` n `26`; metal avg `-0.031` n `20`; unknown avg `1.5372` n `1062`
- 24h: commodity avg `-0.0612` n `13`; crypto_alt avg `-2.0911` n `236`; crypto_major avg `-1.519` n `8`; equity avg `-4.3379` n `151`; fx avg `0.2064` n `6`; index avg `-0.6338` n `26`; metal avg `0.1285` n `20`; unknown avg `-0.777` n `941`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1192`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.081`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0809`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0765`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
