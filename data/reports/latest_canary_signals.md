# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T20:22:32.154831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.2057` n `236`; crypto_major avg `0.0841` n `8`; equity avg `-0.0405` n `151`; fx avg `-0.0004` n `6`; index avg `0.0036` n `26`; metal avg `0.0108` n `20`; unknown avg `4.4511` n `1136`
- 1h: commodity avg `0.0721` n `13`; crypto_alt avg `0.2812` n `236`; crypto_major avg `0.1083` n `8`; equity avg `-0.2255` n `151`; fx avg `0.0149` n `6`; index avg `-0.0407` n `26`; metal avg `-0.0518` n `20`; unknown avg `7.7161` n `1090`
- 4h: commodity avg `0.0947` n `13`; crypto_alt avg `0.9865` n `236`; crypto_major avg `0.5511` n `8`; equity avg `-0.4341` n `151`; fx avg `0.0538` n `6`; index avg `-0.0675` n `26`; metal avg `-0.0166` n `20`; unknown avg `0.8316` n `1088`
- 24h: commodity avg `-0.2061` n `13`; crypto_alt avg `-2.1654` n `236`; crypto_major avg `-1.7217` n `8`; equity avg `-4.1705` n `151`; fx avg `-0.134` n `6`; index avg `-0.5646` n `26`; metal avg `-0.8217` n `20`; unknown avg `1305.6768` n `948`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0836`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0616`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.058`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0554`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
