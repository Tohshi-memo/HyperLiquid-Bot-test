# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T18:22:26.351398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0764` n `12`; crypto_alt avg `-0.048` n `230`; crypto_major avg `-0.0159` n `8`; equity avg `-0.0923` n `102`; fx avg `0.0158` n `6`; index avg `-0.0111` n `25`; metal avg `0.0071` n `20`; unknown avg `7.5637` n `780`
- 1h: commodity avg `0.1173` n `12`; crypto_alt avg `0.2354` n `230`; crypto_major avg `0.3035` n `8`; equity avg `0.2585` n `102`; fx avg `0.0092` n `6`; index avg `0.0162` n `25`; metal avg `0.0902` n `20`; unknown avg `7.6547` n `780`
- 4h: commodity avg `0.0429` n `12`; crypto_alt avg `0.638` n `230`; crypto_major avg `-0.0712` n `8`; equity avg `0.5861` n `102`; fx avg `0.1348` n `6`; index avg `0.1705` n `25`; metal avg `0.26` n `20`; unknown avg `9.9147` n `780`
- 24h: commodity avg `0.2178` n `12`; crypto_alt avg `-0.1006` n `230`; crypto_major avg `-1.6408` n `8`; equity avg `0.7734` n `102`; fx avg `0.234` n `6`; index avg `0.2891` n `25`; metal avg `-0.2662` n `20`; unknown avg `0.3757` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
