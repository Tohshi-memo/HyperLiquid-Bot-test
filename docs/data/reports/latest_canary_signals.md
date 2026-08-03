# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T08:40:18.951051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0469` n `12`; crypto_alt avg `0.068` n `230`; crypto_major avg `0.0312` n `8`; equity avg `0.086` n `102`; fx avg `0.0093` n `6`; index avg `0.0325` n `25`; metal avg `0.0225` n `20`; unknown avg `-0.0018` n `784`
- 1h: commodity avg `0.0932` n `12`; crypto_alt avg `-0.1851` n `230`; crypto_major avg `-0.2776` n `8`; equity avg `-0.5141` n `102`; fx avg `0.0217` n `6`; index avg `-0.0424` n `25`; metal avg `0.0178` n `20`; unknown avg `-0.1123` n `784`
- 4h: commodity avg `0.1493` n `12`; crypto_alt avg `-0.4711` n `230`; crypto_major avg `-0.7726` n `8`; equity avg `-0.9367` n `102`; fx avg `0.0276` n `6`; index avg `-0.0986` n `25`; metal avg `-0.0774` n `20`; unknown avg `-0.0216` n `768`
- 24h: commodity avg `-0.0246` n `12`; crypto_alt avg `-1.2525` n `230`; crypto_major avg `-0.9563` n `8`; equity avg `-0.229` n `102`; fx avg `-0.1692` n `6`; index avg `-0.086` n `25`; metal avg `-0.0873` n `20`; unknown avg `0.9675` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
