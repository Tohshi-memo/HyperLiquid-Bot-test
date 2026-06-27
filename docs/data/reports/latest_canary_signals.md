# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T06:22:29.251295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.1454` n `228`; crypto_major avg `-0.0101` n `8`; equity avg `0.0218` n `88`; fx avg `0.0037` n `6`; index avg `0.0002` n `23`; metal avg `0.0051` n `20`; unknown avg `-0.2083` n `764`
- 1h: commodity avg `-0.0446` n `12`; crypto_alt avg `-0.1106` n `228`; crypto_major avg `-0.2068` n `8`; equity avg `-0.0293` n `88`; fx avg `0.0046` n `6`; index avg `-0.007` n `23`; metal avg `0.0065` n `20`; unknown avg `-0.2911` n `732`
- 4h: commodity avg `0.1196` n `12`; crypto_alt avg `-0.5455` n `228`; crypto_major avg `-0.494` n `8`; equity avg `-0.0319` n `88`; fx avg `0.0052` n `6`; index avg `-0.0207` n `23`; metal avg `-0.0006` n `20`; unknown avg `-0.698` n `732`
- 24h: commodity avg `-0.2669` n `12`; crypto_alt avg `1.5753` n `228`; crypto_major avg `1.1326` n `8`; equity avg `1.6335` n `87`; fx avg `0.0954` n `6`; index avg `0.0723` n `23`; metal avg `0.8973` n `20`; unknown avg `-0.4142` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2047`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
