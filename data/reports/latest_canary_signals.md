# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T19:52:41.473797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0561` n `12`; crypto_alt avg `-0.26` n `228`; crypto_major avg `-0.3021` n `8`; equity avg `-0.0102` n `74`; fx avg `-0.0082` n `6`; index avg `-0.02` n `23`; metal avg `0.0027` n `18`; unknown avg `-0.0727` n `517`
- 1h: commodity avg `0.0813` n `12`; crypto_alt avg `-0.1699` n `228`; crypto_major avg `-0.185` n `8`; equity avg `-0.3907` n `74`; fx avg `-0.0224` n `6`; index avg `-0.2962` n `23`; metal avg `-0.0654` n `18`; unknown avg `-0.0814` n `517`
- 4h: commodity avg `-0.023` n `12`; crypto_alt avg `-0.06` n `228`; crypto_major avg `-0.5245` n `8`; equity avg `-0.7785` n `74`; fx avg `-0.047` n `6`; index avg `-0.5803` n `23`; metal avg `-0.338` n `18`; unknown avg `-0.1753` n `517`
- 24h: commodity avg `-1.1365` n `12`; crypto_alt avg `4.269` n `228`; crypto_major avg `4.4835` n `8`; equity avg `2.6592` n `74`; fx avg `-0.3242` n `6`; index avg `1.0176` n `23`; metal avg `0.0981` n `18`; unknown avg `-1.4141` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
