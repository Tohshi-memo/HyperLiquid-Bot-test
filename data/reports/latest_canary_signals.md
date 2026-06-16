# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T02:52:40.586422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1218` n `12`; crypto_alt avg `0.162` n `228`; crypto_major avg `0.0563` n `8`; equity avg `-0.0506` n `77`; fx avg `0.0028` n `6`; index avg `-0.0422` n `23`; metal avg `0.0121` n `18`; unknown avg `0.0529` n `679`
- 1h: commodity avg `-0.1395` n `12`; crypto_alt avg `-0.7848` n `228`; crypto_major avg `-0.805` n `8`; equity avg `-0.1032` n `77`; fx avg `-0.0298` n `6`; index avg `-0.0108` n `23`; metal avg `0.0698` n `18`; unknown avg `1.0059` n `679`
- 4h: commodity avg `-0.3143` n `12`; crypto_alt avg `-0.3922` n `228`; crypto_major avg `-0.5902` n `8`; equity avg `-0.38` n `77`; fx avg `-0.1189` n `6`; index avg `-0.1186` n `23`; metal avg `-0.3788` n `18`; unknown avg `-0.1764` n `671`
- 24h: commodity avg `0.682` n `12`; crypto_alt avg `-0.1349` n `228`; crypto_major avg `1.4327` n `8`; equity avg `0.8561` n `76`; fx avg `-0.07` n `6`; index avg `0.5194` n `23`; metal avg `-0.8275` n `18`; unknown avg `1.0441` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
