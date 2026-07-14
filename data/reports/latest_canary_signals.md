# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T04:16:30.431756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.0507` n `230`; crypto_major avg `-0.0812` n `8`; equity avg `-0.1526` n `92`; fx avg `0.0088` n `6`; index avg `-0.0623` n `25`; metal avg `-0.0281` n `20`; unknown avg `-0.0432` n `766`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `0.4672` n `230`; crypto_major avg `0.494` n `8`; equity avg `0.5221` n `92`; fx avg `-0.0051` n `6`; index avg `0.1549` n `25`; metal avg `0.0888` n `20`; unknown avg `0.131` n `766`
- 4h: commodity avg `-0.1832` n `12`; crypto_alt avg `-0.0266` n `230`; crypto_major avg `-0.0041` n `8`; equity avg `-0.4302` n `92`; fx avg `-0.0591` n `6`; index avg `-0.0832` n `25`; metal avg `0.2218` n `20`; unknown avg `-0.4456` n `766`
- 24h: commodity avg `1.0273` n `12`; crypto_alt avg `-0.5793` n `230`; crypto_major avg `-1.0422` n `8`; equity avg `-1.5055` n `92`; fx avg `-0.205` n `6`; index avg `-0.3068` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.3054` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
