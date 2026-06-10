# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T03:37:34.115929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0816` n `12`; crypto_alt avg `0.0705` n `228`; crypto_major avg `0.1497` n `8`; equity avg `-0.12` n `74`; fx avg `-0.0138` n `6`; index avg `-0.0296` n `23`; metal avg `0.0975` n `18`; unknown avg `0.1882` n `547`
- 1h: commodity avg `0.0258` n `12`; crypto_alt avg `0.2371` n `228`; crypto_major avg `0.3301` n `8`; equity avg `0.052` n `74`; fx avg `0.015` n `6`; index avg `-0.0999` n `23`; metal avg `-0.1455` n `18`; unknown avg `0.0425` n `547`
- 4h: commodity avg `-0.1176` n `12`; crypto_alt avg `-0.3523` n `228`; crypto_major avg `-0.4989` n `8`; equity avg `-0.2055` n `74`; fx avg `0.0075` n `6`; index avg `-0.1385` n `23`; metal avg `-0.9871` n `18`; unknown avg `-0.316` n `547`
- 24h: commodity avg `-0.4711` n `12`; crypto_alt avg `0.3061` n `228`; crypto_major avg `-2.4138` n `8`; equity avg `-2.8511` n `74`; fx avg `0.1219` n `6`; index avg `-1.2598` n `23`; metal avg `-2.8882` n `18`; unknown avg `-0.2411` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0421`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0387`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.037`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0358`, n `668`, weak_sample_signal
