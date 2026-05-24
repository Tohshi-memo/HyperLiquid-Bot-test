# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T18:22:12.918084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0514` n `12`; crypto_alt avg `0.0635` n `228`; crypto_major avg `0.0337` n `8`; equity avg `0.0162` n `67`; fx avg `0.0` n `6`; index avg `-0.0039` n `23`; metal avg `-0.0156` n `18`; unknown avg `-0.0257` n `396`
- 1h: commodity avg `0.1265` n `12`; crypto_alt avg `0.1173` n `228`; crypto_major avg `-0.0183` n `8`; equity avg `0.0715` n `67`; fx avg `-0.0104` n `6`; index avg `0.0827` n `23`; metal avg `0.0279` n `18`; unknown avg `0.09` n `396`
- 4h: commodity avg `-0.038` n `12`; crypto_alt avg `0.6936` n `228`; crypto_major avg `0.2316` n `8`; equity avg `0.1252` n `67`; fx avg `0.0047` n `6`; index avg `-0.0807` n `23`; metal avg `0.1508` n `18`; unknown avg `-0.2126` n `396`
- 24h: commodity avg `-0.8256` n `12`; crypto_alt avg `-0.3109` n `228`; crypto_major avg `1.4725` n `8`; equity avg `1.4906` n `67`; fx avg `0.0824` n `6`; index avg `0.5713` n `23`; metal avg `0.4939` n `18`; unknown avg `0.6871` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
