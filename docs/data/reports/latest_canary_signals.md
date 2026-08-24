# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T20:38:39.094192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `0.4128` n `231`; crypto_major avg `0.4373` n `8`; equity avg `0.0397` n `122`; fx avg `0.0054` n `6`; index avg `-0.004` n `25`; metal avg `-0.0121` n `20`; unknown avg `-0.0875` n `794`
- 1h: commodity avg `-0.1136` n `12`; crypto_alt avg `0.1498` n `231`; crypto_major avg `0.143` n `8`; equity avg `-0.121` n `122`; fx avg `-0.0004` n `6`; index avg `-0.0329` n `25`; metal avg `0.0272` n `20`; unknown avg `-0.0258` n `794`
- 4h: commodity avg `-0.1339` n `12`; crypto_alt avg `-0.9628` n `231`; crypto_major avg `-0.9907` n `8`; equity avg `-0.5428` n `122`; fx avg `0.0055` n `6`; index avg `-0.062` n `25`; metal avg `-0.0821` n `20`; unknown avg `-0.604` n `793`
- 24h: commodity avg `-0.2894` n `12`; crypto_alt avg `-1.3041` n `231`; crypto_major avg `-0.3426` n `8`; equity avg `-2.8586` n `122`; fx avg `-0.0658` n `6`; index avg `-0.3686` n `25`; metal avg `0.0709` n `20`; unknown avg `1.7008` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
