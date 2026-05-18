# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T21:22:19.360482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1093` n `12`; crypto_alt avg `0.4218` n `228`; crypto_major avg `0.4943` n `8`; equity avg `0.1667` n `66`; fx avg `-0.0216` n `6`; index avg `0.0778` n `23`; metal avg `0.0276` n `18`; unknown avg `1.0631` n `383`
- 1h: commodity avg `0.3118` n `12`; crypto_alt avg `0.0948` n `228`; crypto_major avg `0.166` n `8`; equity avg `0.1489` n `66`; fx avg `-0.0339` n `6`; index avg `0.0591` n `23`; metal avg `0.078` n `18`; unknown avg `0.9818` n `383`
- 4h: commodity avg `-0.1949` n `12`; crypto_alt avg `0.9104` n `228`; crypto_major avg `1.0369` n `8`; equity avg `0.4519` n `66`; fx avg `-0.0621` n `6`; index avg `0.2306` n `23`; metal avg `0.3307` n `18`; unknown avg `1.4695` n `383`
- 24h: commodity avg `0.9595` n `12`; crypto_alt avg `-1.8704` n `228`; crypto_major avg `-1.9801` n `8`; equity avg `-0.8694` n `66`; fx avg `0.1782` n `6`; index avg `-0.356` n `23`; metal avg `1.146` n `18`; unknown avg `1.0414` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
