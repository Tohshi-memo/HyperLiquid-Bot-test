# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T10:22:34.025006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `13`; crypto_alt avg `-0.0551` n `235`; crypto_major avg `-0.0615` n `8`; equity avg `-0.0164` n `151`; fx avg `0.018` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0244` n `20`; unknown avg `-0.0807` n `1135`
- 1h: commodity avg `-0.0478` n `13`; crypto_alt avg `-0.4464` n `235`; crypto_major avg `-0.1418` n `8`; equity avg `-0.1479` n `151`; fx avg `0.0026` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0129` n `20`; unknown avg `0.5371` n `1133`
- 4h: commodity avg `-0.1898` n `13`; crypto_alt avg `-1.2052` n `235`; crypto_major avg `-0.6727` n `8`; equity avg `0.2521` n `151`; fx avg `-0.0523` n `6`; index avg `0.0775` n `26`; metal avg `0.0332` n `20`; unknown avg `0.3231` n `1117`
- 24h: commodity avg `-0.0325` n `13`; crypto_alt avg `-4.0238` n `235`; crypto_major avg `-2.2906` n `8`; equity avg `-2.7959` n `151`; fx avg `0.0401` n `6`; index avg `-0.3126` n `26`; metal avg `-0.0134` n `20`; unknown avg `0.0633` n `973`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1815`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1653`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1644`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1438`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0746`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
