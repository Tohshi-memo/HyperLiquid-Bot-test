# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T16:52:15.209028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1336` n `12`; crypto_alt avg `0.258` n `228`; crypto_major avg `0.1555` n `8`; equity avg `0.282` n `66`; fx avg `0.0047` n `6`; index avg `0.1764` n `23`; metal avg `0.0619` n `18`; unknown avg `-0.0147` n `383`
- 1h: commodity avg `-0.0178` n `12`; crypto_alt avg `0.527` n `228`; crypto_major avg `0.3378` n `8`; equity avg `0.8781` n `66`; fx avg `-0.0786` n `6`; index avg `0.5108` n `23`; metal avg `0.2864` n `18`; unknown avg `-0.1346` n `383`
- 4h: commodity avg `0.1854` n `12`; crypto_alt avg `-0.0027` n `228`; crypto_major avg `-0.0452` n `8`; equity avg `0.9073` n `66`; fx avg `-0.0782` n `6`; index avg `0.1001` n `23`; metal avg `-1.0494` n `18`; unknown avg `-0.4241` n `383`
- 24h: commodity avg `0.544` n `12`; crypto_alt avg `0.9699` n `228`; crypto_major avg `1.0726` n `8`; equity avg `0.6091` n `66`; fx avg `-0.0714` n `6`; index avg `-0.2293` n `23`; metal avg `-1.8181` n `18`; unknown avg `-0.148` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
