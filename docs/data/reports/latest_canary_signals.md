# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T14:22:25.244546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `12`; crypto_alt avg `-0.2499` n `228`; crypto_major avg `-0.2797` n `8`; equity avg `-0.2797` n `66`; fx avg `0.0047` n `6`; index avg `-0.1591` n `23`; metal avg `-0.2303` n `18`; unknown avg `0.1448` n `383`
- 1h: commodity avg `0.0162` n `12`; crypto_alt avg `-0.3748` n `228`; crypto_major avg `-0.2801` n `8`; equity avg `-0.72` n `66`; fx avg `-0.0231` n `6`; index avg `-0.7517` n `23`; metal avg `-0.6508` n `18`; unknown avg `0.0217` n `383`
- 4h: commodity avg `0.2647` n `12`; crypto_alt avg `-0.4273` n `228`; crypto_major avg `-0.3578` n `8`; equity avg `-1.0303` n `66`; fx avg `-0.07` n `6`; index avg `-0.8346` n `23`; metal avg `-1.377` n `18`; unknown avg `-0.3739` n `383`
- 24h: commodity avg `1.27` n `12`; crypto_alt avg `0.4729` n `228`; crypto_major avg `0.1848` n `8`; equity avg `-2.2982` n `66`; fx avg `0.1985` n `6`; index avg `-1.6738` n `23`; metal avg `-2.087` n `18`; unknown avg `-0.3306` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
