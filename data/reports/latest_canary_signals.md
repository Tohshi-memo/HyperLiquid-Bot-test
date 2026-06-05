# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T22:22:24.465139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6188` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1191` n `12`; crypto_alt avg `0.4383` n `228`; crypto_major avg `0.3957` n `8`; equity avg `-0.0688` n `74`; fx avg `0.0014` n `6`; index avg `-0.0528` n `23`; metal avg `-0.0046` n `18`; unknown avg `0.1013` n `425`
- 1h: commodity avg `-0.4435` n `12`; crypto_alt avg `-0.1219` n `228`; crypto_major avg `-0.2514` n `8`; equity avg `0.0364` n `74`; fx avg `0.0282` n `6`; index avg `0.0085` n `23`; metal avg `0.058` n `18`; unknown avg `0.9645` n `425`
- 4h: commodity avg `-0.2802` n `12`; crypto_alt avg `1.7251` n `228`; crypto_major avg `1.552` n `8`; equity avg `0.2796` n `74`; fx avg `-0.0077` n `6`; index avg `-0.5088` n `23`; metal avg `-0.0668` n `18`; unknown avg `2.235` n `424`
- 24h: commodity avg `-1.7596` n `12`; crypto_alt avg `-5.252` n `228`; crypto_major avg `-4.8802` n `8`; equity avg `-5.817` n `74`; fx avg `-0.0393` n `6`; index avg `-4.1524` n `23`; metal avg `-4.4759` n `18`; unknown avg `-1.4729` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
