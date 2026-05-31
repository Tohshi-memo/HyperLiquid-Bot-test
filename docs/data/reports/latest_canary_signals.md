# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T10:37:18.442307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0947` n `12`; crypto_alt avg `0.1503` n `228`; crypto_major avg `0.0287` n `8`; equity avg `-0.0246` n `69`; fx avg `-0.0006` n `6`; index avg `-0.0254` n `23`; metal avg `0.003` n `18`; unknown avg `-0.1578` n `421`
- 1h: commodity avg `-0.048` n `12`; crypto_alt avg `-0.3983` n `228`; crypto_major avg `-0.211` n `8`; equity avg `-0.0793` n `69`; fx avg `-0.0026` n `6`; index avg `0.015` n `23`; metal avg `-0.0135` n `18`; unknown avg `-0.0522` n `421`
- 4h: commodity avg `0.1116` n `12`; crypto_alt avg `-0.6929` n `228`; crypto_major avg `-0.671` n `8`; equity avg `0.1265` n `69`; fx avg `-0.0135` n `6`; index avg `-0.0805` n `23`; metal avg `-0.0181` n `18`; unknown avg `-0.3761` n `421`
- 24h: commodity avg `0.1935` n `12`; crypto_alt avg `-0.2222` n `228`; crypto_major avg `1.2101` n `8`; equity avg `1.02` n `69`; fx avg `0.0163` n `6`; index avg `-0.0647` n `23`; metal avg `-0.0988` n `18`; unknown avg `0.5362` n `401`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
