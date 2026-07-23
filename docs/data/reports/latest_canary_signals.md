# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T13:37:26.030094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.1344` n `230`; crypto_major avg `-0.095` n `8`; equity avg `0.6607` n `100`; fx avg `-0.0128` n `6`; index avg `0.1366` n `25`; metal avg `0.1202` n `20`; unknown avg `0.0947` n `772`
- 1h: commodity avg `-0.0986` n `12`; crypto_alt avg `-0.0185` n `230`; crypto_major avg `-0.2701` n `8`; equity avg `0.2458` n `100`; fx avg `-0.0281` n `6`; index avg `0.0426` n `25`; metal avg `-0.0349` n `20`; unknown avg `-0.0613` n `772`
- 4h: commodity avg `0.1081` n `12`; crypto_alt avg `-0.5563` n `230`; crypto_major avg `-0.947` n `8`; equity avg `-1.0744` n `99`; fx avg `-0.0262` n `6`; index avg `-0.201` n `25`; metal avg `-0.2826` n `20`; unknown avg `0.1341` n `772`
- 24h: commodity avg `0.8988` n `12`; crypto_alt avg `-0.8094` n `230`; crypto_major avg `-0.9724` n `8`; equity avg `-0.7058` n `99`; fx avg `-0.1178` n `6`; index avg `-0.0734` n `25`; metal avg `-0.701` n `20`; unknown avg `0.061` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
