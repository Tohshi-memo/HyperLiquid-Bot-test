# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T02:07:20.785143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.2631` n `228`; crypto_major avg `0.0632` n `8`; equity avg `0.0218` n `69`; fx avg `-0.0005` n `6`; index avg `0.0147` n `23`; metal avg `-0.0031` n `18`; unknown avg `-0.1745` n `421`
- 1h: commodity avg `0.0695` n `12`; crypto_alt avg `0.3586` n `228`; crypto_major avg `0.1025` n `8`; equity avg `0.0383` n `69`; fx avg `0.0042` n `6`; index avg `0.023` n `23`; metal avg `0.0042` n `18`; unknown avg `1.013` n `421`
- 4h: commodity avg `0.0983` n `12`; crypto_alt avg `0.6088` n `228`; crypto_major avg `0.8809` n `8`; equity avg `0.2858` n `69`; fx avg `-0.0042` n `6`; index avg `0.0533` n `23`; metal avg `-0.0099` n `18`; unknown avg `-0.2628` n `421`
- 24h: commodity avg `-0.1672` n `12`; crypto_alt avg `0.2597` n `228`; crypto_major avg `2.029` n `8`; equity avg `0.9427` n `69`; fx avg `0.0325` n `6`; index avg `0.1304` n `23`; metal avg `-0.0111` n `18`; unknown avg `1.3202` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
