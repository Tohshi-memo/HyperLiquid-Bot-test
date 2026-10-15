# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T12:07:32.384790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `13`; crypto_alt avg `-0.2744` n `236`; crypto_major avg `-0.1813` n `8`; equity avg `-0.1964` n `151`; fx avg `0.0031` n `6`; index avg `-0.0204` n `26`; metal avg `-0.0237` n `20`; unknown avg `0.0185` n `1128`
- 1h: commodity avg `0.0841` n `13`; crypto_alt avg `0.2197` n `236`; crypto_major avg `-0.0397` n `8`; equity avg `0.3716` n `151`; fx avg `0.0123` n `6`; index avg `0.0515` n `26`; metal avg `-0.0334` n `20`; unknown avg `0.6424` n `1128`
- 4h: commodity avg `0.2231` n `13`; crypto_alt avg `-0.0471` n `236`; crypto_major avg `-0.4834` n `8`; equity avg `-0.2` n `151`; fx avg `0.0374` n `6`; index avg `-0.0037` n `26`; metal avg `0.0231` n `20`; unknown avg `-0.2223` n `1048`
- 24h: commodity avg `-0.2687` n `13`; crypto_alt avg `-5.0409` n `236`; crypto_major avg `-3.9537` n `8`; equity avg `-6.0476` n `151`; fx avg `0.0642` n `6`; index avg `-0.9691` n `26`; metal avg `-0.4909` n `20`; unknown avg `2.155` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1214`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1048`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0854`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0676`, n `666`, weak_sample_signal
