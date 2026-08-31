# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T23:07:29.841313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0447` n `12`; crypto_alt avg `-0.0384` n `232`; crypto_major avg `-0.1548` n `8`; equity avg `-0.0391` n `129`; fx avg `-0.0073` n `6`; index avg `0.0008` n `26`; metal avg `0.002` n `20`; unknown avg `0.1316` n `791`
- 1h: commodity avg `0.0619` n `12`; crypto_alt avg `-0.2138` n `232`; crypto_major avg `-0.4919` n `8`; equity avg `-0.0758` n `129`; fx avg `-0.0023` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0268` n `20`; unknown avg `0.6049` n `791`
- 4h: commodity avg `0.139` n `12`; crypto_alt avg `-0.2266` n `232`; crypto_major avg `-0.6622` n `8`; equity avg `0.437` n `129`; fx avg `0.0002` n `6`; index avg `0.0788` n `26`; metal avg `0.0868` n `20`; unknown avg `1.2271` n `773`
- 24h: commodity avg `0.4498` n `12`; crypto_alt avg `0.3352` n `231`; crypto_major avg `0.3306` n `8`; equity avg `0.5158` n `129`; fx avg `-0.0969` n `6`; index avg `-0.0355` n `26`; metal avg `-0.3722` n `20`; unknown avg `0.1574` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
