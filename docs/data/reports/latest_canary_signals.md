# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T14:07:29.298291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0361` n `12`; crypto_alt avg `0.2664` n `230`; crypto_major avg `0.359` n `8`; equity avg `0.1682` n `98`; fx avg `-0.0161` n `6`; index avg `0.0408` n `25`; metal avg `0.0778` n `20`; unknown avg `-0.0224` n `773`
- 1h: commodity avg `-0.018` n `12`; crypto_alt avg `0.7013` n `230`; crypto_major avg `0.8142` n `8`; equity avg `1.3491` n `98`; fx avg `-0.0126` n `6`; index avg `0.1973` n `25`; metal avg `0.2856` n `20`; unknown avg `10.711` n `773`
- 4h: commodity avg `-0.0366` n `12`; crypto_alt avg `0.6056` n `230`; crypto_major avg `0.5625` n `8`; equity avg `0.8882` n `98`; fx avg `-0.0188` n `6`; index avg `0.1056` n `25`; metal avg `0.2577` n `20`; unknown avg `11.2543` n `773`
- 24h: commodity avg `0.5282` n `12`; crypto_alt avg `-0.1651` n `230`; crypto_major avg `-0.9538` n `8`; equity avg `0.9882` n `98`; fx avg `-0.0192` n `6`; index avg `0.1001` n `25`; metal avg `0.7285` n `20`; unknown avg `0.765` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1022`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0675`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0631`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0627`, n `666`, weak_sample_signal
