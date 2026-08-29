# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T08:07:24.766749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `-0.2394` n `231`; crypto_major avg `-0.1331` n `8`; equity avg `-0.0111` n `127`; fx avg `0.0038` n `6`; index avg `0.0021` n `26`; metal avg `-0.0018` n `20`; unknown avg `-0.0279` n `793`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.2859` n `231`; crypto_major avg `-0.1374` n `8`; equity avg `0.0146` n `127`; fx avg `0.0057` n `6`; index avg `-0.0` n `26`; metal avg `0.0111` n `20`; unknown avg `0.0192` n `793`
- 4h: commodity avg `-0.0196` n `12`; crypto_alt avg `-0.3108` n `231`; crypto_major avg `-0.1957` n `8`; equity avg `0.0843` n `127`; fx avg `0.0085` n `6`; index avg `0.0051` n `26`; metal avg `0.0065` n `20`; unknown avg `0.1132` n `761`
- 24h: commodity avg `-0.0397` n `12`; crypto_alt avg `-2.2617` n `231`; crypto_major avg `-2.7412` n `8`; equity avg `-1.3401` n `127`; fx avg `-0.0226` n `6`; index avg `-0.1236` n `26`; metal avg `-0.6291` n `20`; unknown avg `-0.4366` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
