# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T16:52:23.937544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5443` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.9865` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5064` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0487` n `12`; crypto_alt avg `1.3171` n `228`; crypto_major avg `1.0805` n `8`; equity avg `0.0344` n `74`; fx avg `-0.0008` n `6`; index avg `-0.0477` n `23`; metal avg `0.1131` n `18`; unknown avg `1.622` n `424`
- 1h: commodity avg `-0.4303` n `12`; crypto_alt avg `1.4084` n `228`; crypto_major avg `1.0375` n `8`; equity avg `-0.949` n `74`; fx avg `-0.0092` n `6`; index avg `-0.6412` n `23`; metal avg `-0.1158` n `18`; unknown avg `2.0189` n `424`
- 4h: commodity avg `-1.2991` n `12`; crypto_alt avg `-0.6573` n `228`; crypto_major avg `-1.3764` n `8`; equity avg `-3.9207` n `74`; fx avg `-0.1552` n `6`; index avg `-2.1755` n `23`; metal avg `-2.8828` n `18`; unknown avg `0.2958` n `424`
- 24h: commodity avg `-1.5261` n `12`; crypto_alt avg `-7.8745` n `228`; crypto_major avg `-6.2269` n `8`; equity avg `-5.896` n `74`; fx avg `-0.0447` n `6`; index avg `-3.111` n `23`; metal avg `-4.0646` n `18`; unknown avg `-0.3282` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
