# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T06:07:17.169963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0311` n `12`; crypto_alt avg `0.0481` n `228`; crypto_major avg `0.0359` n `8`; equity avg `-0.0323` n `66`; fx avg `0.0177` n `6`; index avg `-0.011` n `23`; metal avg `0.2229` n `18`; unknown avg `0.0166` n `363`
- 1h: commodity avg `0.2615` n `12`; crypto_alt avg `-0.0901` n `228`; crypto_major avg `0.0408` n `8`; equity avg `0.0038` n `66`; fx avg `0.0295` n `6`; index avg `0.0261` n `23`; metal avg `-0.004` n `18`; unknown avg `-0.2549` n `363`
- 4h: commodity avg `0.2799` n `12`; crypto_alt avg `0.4338` n `228`; crypto_major avg `0.4252` n `8`; equity avg `0.1498` n `66`; fx avg `0.0742` n `6`; index avg `0.0325` n `23`; metal avg `-0.3431` n `18`; unknown avg `0.0951` n `363`
- 24h: commodity avg `0.3325` n `12`; crypto_alt avg `1.3847` n `228`; crypto_major avg `0.6821` n `8`; equity avg `-0.9104` n `66`; fx avg `0.3104` n `6`; index avg `-0.3651` n `23`; metal avg `0.5875` n `18`; unknown avg `0.5901` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
