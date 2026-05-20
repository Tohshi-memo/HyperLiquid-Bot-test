# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T06:22:18.877652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2993` n `12`; crypto_alt avg `-0.0313` n `228`; crypto_major avg `0.1356` n `8`; equity avg `0.1975` n `66`; fx avg `-0.0089` n `6`; index avg `0.1107` n `23`; metal avg `0.2465` n `18`; unknown avg `-0.069` n `384`
- 1h: commodity avg `-0.2043` n `12`; crypto_alt avg `0.2882` n `228`; crypto_major avg `0.3154` n `8`; equity avg `0.3944` n `66`; fx avg `-0.0188` n `6`; index avg `0.203` n `23`; metal avg `0.4007` n `18`; unknown avg `-0.17` n `374`
- 4h: commodity avg `-0.1179` n `12`; crypto_alt avg `0.8629` n `228`; crypto_major avg `0.7286` n `8`; equity avg `0.0999` n `66`; fx avg `0.0546` n `6`; index avg `-0.0022` n `23`; metal avg `0.2791` n `18`; unknown avg `0.2061` n `374`
- 24h: commodity avg `0.3227` n `12`; crypto_alt avg `-0.2279` n `228`; crypto_major avg `-0.0664` n `8`; equity avg `0.4934` n `66`; fx avg `-0.1664` n `6`; index avg `-0.3746` n `23`; metal avg `-1.6719` n `18`; unknown avg `0.195` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0435`, n `668`, weak_sample_signal
