# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T20:07:28.216984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0513` n `230`; crypto_major avg `-0.0939` n `8`; equity avg `0.0045` n `92`; fx avg `-0.005` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.0199` n `765`
- 1h: commodity avg `0.0759` n `12`; crypto_alt avg `0.0763` n `230`; crypto_major avg `-0.0365` n `8`; equity avg `0.0493` n `92`; fx avg `-0.0229` n `6`; index avg `0.0132` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.0425` n `765`
- 4h: commodity avg `0.1328` n `12`; crypto_alt avg `-0.0874` n `230`; crypto_major avg `-0.0084` n `8`; equity avg `0.1059` n `92`; fx avg `0.001` n `6`; index avg `0.0023` n `25`; metal avg `-0.0146` n `20`; unknown avg `-0.2308` n `759`
- 24h: commodity avg `0.609` n `12`; crypto_alt avg `-1.3856` n `230`; crypto_major avg `-0.5657` n `8`; equity avg `-0.162` n `92`; fx avg `0.001` n `6`; index avg `-0.0936` n `25`; metal avg `-0.1019` n `20`; unknown avg `0.1707` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
