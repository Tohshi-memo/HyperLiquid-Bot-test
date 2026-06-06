# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T06:37:24.085981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1032` n `12`; crypto_alt avg `0.0377` n `228`; crypto_major avg `-0.1457` n `8`; equity avg `-0.0462` n `74`; fx avg `0.0` n `6`; index avg `-0.0354` n `23`; metal avg `-0.0423` n `18`; unknown avg `0.0409` n `425`
- 1h: commodity avg `-0.2572` n `12`; crypto_alt avg `1.3881` n `228`; crypto_major avg `1.1252` n `8`; equity avg `0.4755` n `74`; fx avg `0.0026` n `6`; index avg `0.25` n `23`; metal avg `0.1979` n `18`; unknown avg `0.0732` n `415`
- 4h: commodity avg `-0.4707` n `12`; crypto_alt avg `-0.6926` n `228`; crypto_major avg `0.0487` n `8`; equity avg `0.4298` n `74`; fx avg `-0.0055` n `6`; index avg `-0.0113` n `23`; metal avg `0.0662` n `18`; unknown avg `-0.3697` n `415`
- 24h: commodity avg `-1.4784` n `12`; crypto_alt avg `-2.7996` n `228`; crypto_major avg `-1.8562` n `8`; equity avg `-5.8305` n `74`; fx avg `-0.1756` n `6`; index avg `-4.0335` n `23`; metal avg `-4.0451` n `18`; unknown avg `1.4728` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
