# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T22:52:24.179186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `12`; crypto_alt avg `-0.0814` n `230`; crypto_major avg `-0.0658` n `8`; equity avg `0.0169` n `102`; fx avg `0.0004` n `6`; index avg `-0.0039` n `25`; metal avg `0.016` n `20`; unknown avg `0.0395` n `779`
- 1h: commodity avg `-0.0331` n `12`; crypto_alt avg `0.1313` n `230`; crypto_major avg `0.3269` n `8`; equity avg `0.1576` n `102`; fx avg `0.026` n `6`; index avg `0.0508` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.1217` n `779`
- 4h: commodity avg `0.0685` n `12`; crypto_alt avg `0.2121` n `230`; crypto_major avg `0.3627` n `8`; equity avg `1.5814` n `102`; fx avg `0.0675` n `6`; index avg `0.1969` n `25`; metal avg `0.1331` n `20`; unknown avg `-0.1601` n `779`
- 24h: commodity avg `-0.0589` n `12`; crypto_alt avg `1.0186` n `230`; crypto_major avg `1.8276` n `8`; equity avg `7.6582` n `102`; fx avg `-0.3998` n `6`; index avg `0.9227` n `25`; metal avg `0.5413` n `20`; unknown avg `0.1294` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
