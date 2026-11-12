# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T19:22:41.887013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0928` n `13`; crypto_alt avg `0.2172` n `239`; crypto_major avg `0.054` n `8`; equity avg `0.0878` n `162`; fx avg `0.0182` n `6`; index avg `0.0012` n `27`; metal avg `-0.0038` n `20`; unknown avg `0.1902` n `1259`
- 1h: commodity avg `0.1452` n `13`; crypto_alt avg `0.3398` n `239`; crypto_major avg `-0.1463` n `8`; equity avg `-0.3188` n `162`; fx avg `0.0167` n `6`; index avg `-0.0287` n `27`; metal avg `-0.0279` n `20`; unknown avg `0.7533` n `1253`
- 4h: commodity avg `0.4471` n `13`; crypto_alt avg `1.2204` n `239`; crypto_major avg `0.672` n `8`; equity avg `0.8436` n `162`; fx avg `-0.0062` n `6`; index avg `0.0627` n `27`; metal avg `0.1887` n `20`; unknown avg `60.7914` n `1231`
- 24h: commodity avg `0.6468` n `13`; crypto_alt avg `-2.3688` n `239`; crypto_major avg `-2.9418` n `8`; equity avg `-2.5665` n `162`; fx avg `-0.1423` n `6`; index avg `-0.1597` n `27`; metal avg `-0.72` n `20`; unknown avg `15.7698` n `1139`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
