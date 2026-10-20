# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T10:37:29.487771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `13`; crypto_alt avg `0.0176` n `237`; crypto_major avg `-0.0613` n `8`; equity avg `-0.1009` n `151`; fx avg `-0.0004` n `6`; index avg `-0.0258` n `26`; metal avg `-0.006` n `20`; unknown avg `3.7039` n `1198`
- 1h: commodity avg `-0.0421` n `13`; crypto_alt avg `0.0854` n `237`; crypto_major avg `0.0704` n `8`; equity avg `-0.0462` n `151`; fx avg `-0.0002` n `6`; index avg `0.0042` n `26`; metal avg `-0.0147` n `20`; unknown avg `3.9941` n `1196`
- 4h: commodity avg `0.2188` n `13`; crypto_alt avg `-0.5396` n `237`; crypto_major avg `-0.4118` n `8`; equity avg `-0.4525` n `151`; fx avg `-0.0148` n `6`; index avg `-0.0721` n `26`; metal avg `-0.0617` n `20`; unknown avg `0.7163` n `1180`
- 24h: commodity avg `0.1595` n `13`; crypto_alt avg `0.3206` n `237`; crypto_major avg `-0.3935` n `8`; equity avg `-1.7603` n `151`; fx avg `-0.0123` n `6`; index avg `-0.266` n `26`; metal avg `-0.2628` n `20`; unknown avg `0.3305` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
