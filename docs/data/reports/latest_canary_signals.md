# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T14:43:23.870563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `0.0196` n `230`; crypto_major avg `0.0305` n `8`; equity avg `0.011` n `114`; fx avg `0.0001` n `6`; index avg `-0.0054` n `25`; metal avg `0.0038` n `20`; unknown avg `0.0032` n `791`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `0.0456` n `230`; crypto_major avg `-0.09` n `8`; equity avg `0.0335` n `114`; fx avg `-0.001` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0013` n `20`; unknown avg `0.006` n `791`
- 4h: commodity avg `0.0547` n `12`; crypto_alt avg `0.0032` n `230`; crypto_major avg `0.092` n `8`; equity avg `0.0554` n `114`; fx avg `-0.0057` n `6`; index avg `0.0144` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0537` n `791`
- 24h: commodity avg `-0.0781` n `12`; crypto_alt avg `1.2` n `230`; crypto_major avg `0.4631` n `8`; equity avg `-0.3714` n `114`; fx avg `0.0853` n `6`; index avg `-0.0659` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.0188` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
