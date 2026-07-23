# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T23:52:28.194182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0857` n `230`; crypto_major avg `-0.18` n `8`; equity avg `-0.0027` n `100`; fx avg `0.0062` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.2328` n `772`
- 1h: commodity avg `0.0141` n `12`; crypto_alt avg `-0.124` n `230`; crypto_major avg `-0.1426` n `8`; equity avg `-0.1107` n `100`; fx avg `-0.0043` n `6`; index avg `-0.0147` n `25`; metal avg `-0.0341` n `20`; unknown avg `-0.2744` n `772`
- 4h: commodity avg `0.088` n `12`; crypto_alt avg `0.051` n `230`; crypto_major avg `0.2741` n `8`; equity avg `0.3542` n `100`; fx avg `-0.0096` n `6`; index avg `0.0876` n `25`; metal avg `0.006` n `20`; unknown avg `-0.1` n `772`
- 24h: commodity avg `0.7102` n `12`; crypto_alt avg `-1.6534` n `230`; crypto_major avg `-2.3042` n `8`; equity avg `-1.4132` n `99`; fx avg `-0.0697` n `6`; index avg `-0.2798` n `25`; metal avg `-0.7413` n `20`; unknown avg `-0.2862` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
