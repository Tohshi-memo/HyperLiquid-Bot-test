# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T22:37:37.541081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.43` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.3367` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `-0.0451` n `228`; crypto_major avg `-0.073` n `8`; equity avg `0.0123` n `77`; fx avg `0.0021` n `6`; index avg `-0.0008` n `23`; metal avg `0.0735` n `18`; unknown avg `0.0412` n `687`
- 1h: commodity avg `0.0377` n `12`; crypto_alt avg `-0.6876` n `228`; crypto_major avg `-0.5948` n `8`; equity avg `-0.1969` n `77`; fx avg `-0.002` n `6`; index avg `-0.1376` n `23`; metal avg `-0.0504` n `18`; unknown avg `0.4157` n `687`
- 4h: commodity avg `0.139` n `12`; crypto_alt avg `-1.5271` n `228`; crypto_major avg `-1.4583` n `8`; equity avg `-0.201` n `77`; fx avg `-0.0237` n `6`; index avg `-0.1216` n `23`; metal avg `-0.258` n `18`; unknown avg `0.3039` n `679`
- 24h: commodity avg `0.1457` n `12`; crypto_alt avg `1.123` n `228`; crypto_major avg `2.7396` n `8`; equity avg `1.618` n `76`; fx avg `-0.0765` n `6`; index avg `0.8998` n `23`; metal avg `0.4435` n `18`; unknown avg `2.5324` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
