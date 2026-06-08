# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T22:37:23.659898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.1545` n `228`; crypto_major avg `-0.0282` n `8`; equity avg `-0.0132` n `74`; fx avg `0.002` n `6`; index avg `-0.0` n `23`; metal avg `0.0211` n `18`; unknown avg `-0.3798` n `517`
- 1h: commodity avg `-0.1341` n `12`; crypto_alt avg `-1.0531` n `228`; crypto_major avg `-0.857` n `8`; equity avg `-0.2412` n `74`; fx avg `0.0962` n `6`; index avg `0.0066` n `23`; metal avg `-0.1807` n `18`; unknown avg `-0.3369` n `517`
- 4h: commodity avg `0.0372` n `12`; crypto_alt avg `-0.6955` n `228`; crypto_major avg `-0.1699` n `8`; equity avg `-0.4611` n `74`; fx avg `-0.0197` n `6`; index avg `-0.2071` n `23`; metal avg `-0.0512` n `18`; unknown avg `-0.6314` n `517`
- 24h: commodity avg `-0.7592` n `12`; crypto_alt avg `0.4256` n `228`; crypto_major avg `1.1623` n `8`; equity avg `1.7445` n `74`; fx avg `-0.2727` n `6`; index avg `0.9222` n `23`; metal avg `0.0835` n `18`; unknown avg `-2.7053` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
