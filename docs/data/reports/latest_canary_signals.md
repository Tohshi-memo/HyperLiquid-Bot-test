# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T03:37:13.595359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0785` n `12`; crypto_alt avg `0.1605` n `228`; crypto_major avg `0.0718` n `8`; equity avg `0.1664` n `66`; fx avg `0.0206` n `6`; index avg `0.0765` n `23`; metal avg `0.1831` n `18`; unknown avg `0.4355` n `384`
- 1h: commodity avg `-0.2254` n `12`; crypto_alt avg `0.0764` n `228`; crypto_major avg `0.194` n `8`; equity avg `0.1791` n `66`; fx avg `0.0151` n `6`; index avg `0.0533` n `23`; metal avg `0.2399` n `18`; unknown avg `17.4968` n `384`
- 4h: commodity avg `-0.143` n `12`; crypto_alt avg `0.1567` n `228`; crypto_major avg `-0.3367` n `8`; equity avg `-0.3162` n `66`; fx avg `-0.0065` n `6`; index avg `-0.4182` n `23`; metal avg `-0.4675` n `18`; unknown avg `-0.5273` n `383`
- 24h: commodity avg `0.6446` n `12`; crypto_alt avg `-0.882` n `228`; crypto_major avg `-0.7406` n `8`; equity avg `-0.1133` n `66`; fx avg `-0.1117` n `6`; index avg `-0.7268` n `23`; metal avg `-2.0669` n `18`; unknown avg `0.9583` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
