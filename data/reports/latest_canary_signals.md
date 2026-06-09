# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T06:07:22.802999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `-0.0516` n `228`; crypto_major avg `0.0118` n `8`; equity avg `0.0514` n `74`; fx avg `-0.0227` n `6`; index avg `-0.0486` n `23`; metal avg `-0.0461` n `18`; unknown avg `-0.0412` n `505`
- 1h: commodity avg `-0.1277` n `12`; crypto_alt avg `0.3775` n `228`; crypto_major avg `0.4768` n `8`; equity avg `0.2611` n `74`; fx avg `-0.0728` n `6`; index avg `0.073` n `23`; metal avg `0.2555` n `18`; unknown avg `59.4045` n `505`
- 4h: commodity avg `-0.2599` n `12`; crypto_alt avg `0.8475` n `228`; crypto_major avg `1.0192` n `8`; equity avg `1.1009` n `74`; fx avg `-0.0482` n `6`; index avg `0.516` n `23`; metal avg `0.371` n `18`; unknown avg `0.2645` n `505`
- 24h: commodity avg `-1.5321` n `12`; crypto_alt avg `0.9388` n `228`; crypto_major avg `1.4043` n `8`; equity avg `3.3861` n `74`; fx avg `-0.2393` n `6`; index avg `1.5038` n `23`; metal avg `1.003` n `18`; unknown avg `-2.8454` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
