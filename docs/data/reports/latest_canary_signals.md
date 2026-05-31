# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T03:07:18.787032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0788` n `12`; crypto_alt avg `0.1337` n `228`; crypto_major avg `0.0208` n `8`; equity avg `0.0468` n `69`; fx avg `-0.0001` n `6`; index avg `0.0433` n `23`; metal avg `0.0101` n `18`; unknown avg `-0.0759` n `421`
- 1h: commodity avg `-0.0958` n `12`; crypto_alt avg `-0.1824` n `228`; crypto_major avg `0.0385` n `8`; equity avg `0.0527` n `69`; fx avg `0.0142` n `6`; index avg `-0.0243` n `23`; metal avg `-0.0385` n `18`; unknown avg `-0.1467` n `419`
- 4h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.4879` n `228`; crypto_major avg `0.6822` n `8`; equity avg `0.1973` n `69`; fx avg `0.0236` n `6`; index avg `0.016` n `23`; metal avg `-0.0363` n `18`; unknown avg `-0.0499` n `419`
- 24h: commodity avg `-0.1214` n `12`; crypto_alt avg `-0.1014` n `228`; crypto_major avg `1.9899` n `8`; equity avg `0.9493` n `69`; fx avg `0.0463` n `6`; index avg `0.1225` n `23`; metal avg `-0.0591` n `18`; unknown avg `1.3454` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
