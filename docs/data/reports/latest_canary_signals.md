# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T08:07:20.338430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0739` n `12`; crypto_alt avg `-0.3637` n `228`; crypto_major avg `-0.167` n `8`; equity avg `-0.1972` n `66`; fx avg `-0.0088` n `6`; index avg `-0.0833` n `23`; metal avg `-0.1525` n `18`; unknown avg `0.0383` n `383`
- 1h: commodity avg `-0.0926` n `12`; crypto_alt avg `-0.1208` n `228`; crypto_major avg `0.1381` n `8`; equity avg `0.0814` n `66`; fx avg `0.0108` n `6`; index avg `0.0545` n `23`; metal avg `-0.0749` n `18`; unknown avg `0.0577` n `383`
- 4h: commodity avg `0.2475` n `12`; crypto_alt avg `0.0201` n `228`; crypto_major avg `0.185` n `8`; equity avg `0.44` n `66`; fx avg `0.0011` n `6`; index avg `0.2825` n `23`; metal avg `0.0749` n `18`; unknown avg `0.3141` n `363`
- 24h: commodity avg `0.7956` n `12`; crypto_alt avg `1.5718` n `228`; crypto_major avg `0.9299` n `8`; equity avg `-0.9068` n `66`; fx avg `0.3102` n `6`; index avg `-0.3249` n `23`; metal avg `-0.0137` n `18`; unknown avg `0.8675` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
