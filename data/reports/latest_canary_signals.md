# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T10:22:30.465844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.1584` n `228`; crypto_major avg `0.0016` n `8`; equity avg `-0.0229` n `66`; fx avg `-0.0057` n `5`; index avg `0.0186` n `23`; metal avg `-0.1016` n `18`; unknown avg `-0.0027` n `383`
- 1h: commodity avg `0.0421` n `12`; crypto_alt avg `-0.5091` n `228`; crypto_major avg `-0.309` n `8`; equity avg `-0.3266` n `66`; fx avg `0.0365` n `5`; index avg `-0.1057` n `23`; metal avg `-0.2098` n `18`; unknown avg `-0.0942` n `383`
- 4h: commodity avg `-0.1708` n `12`; crypto_alt avg `-0.4756` n `228`; crypto_major avg `-0.0914` n `8`; equity avg `0.5791` n `66`; fx avg `0.0348` n `5`; index avg `0.2189` n `23`; metal avg `0.2936` n `18`; unknown avg `-0.4841` n `383`
- 24h: commodity avg `0.7918` n `12`; crypto_alt avg `-3.7403` n `228`; crypto_major avg `-2.0813` n `8`; equity avg `0.0747` n `65`; fx avg `0.0841` n `5`; index avg `0.1194` n `23`; metal avg `-0.0585` n `18`; unknown avg `-0.7165` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
