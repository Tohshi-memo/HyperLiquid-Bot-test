# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T23:37:27.379151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0535` n `232`; crypto_major avg `-0.0388` n `8`; equity avg `0.0514` n `129`; fx avg `-0.0025` n `6`; index avg `0.0136` n `26`; metal avg `0.0176` n `20`; unknown avg `-0.1277` n `793`
- 1h: commodity avg `0.0302` n `12`; crypto_alt avg `-0.0487` n `232`; crypto_major avg `-0.1908` n `8`; equity avg `-0.0258` n `129`; fx avg `-0.0143` n `6`; index avg `0.0102` n `26`; metal avg `-0.0208` n `20`; unknown avg `-0.0219` n `791`
- 4h: commodity avg `0.1041` n `12`; crypto_alt avg `0.1061` n `232`; crypto_major avg `-0.3732` n `8`; equity avg `0.3372` n `129`; fx avg `-0.0002` n `6`; index avg `0.0563` n `26`; metal avg `-0.0032` n `20`; unknown avg `1.3083` n `773`
- 24h: commodity avg `0.4596` n `12`; crypto_alt avg `1.9729` n `231`; crypto_major avg `1.6522` n `8`; equity avg `0.9513` n `129`; fx avg `-0.1054` n `6`; index avg `0.056` n `26`; metal avg `-0.2932` n `20`; unknown avg `0.3192` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
