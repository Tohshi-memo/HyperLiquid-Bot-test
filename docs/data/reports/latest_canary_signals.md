# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T11:07:24.752852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0565` n `12`; crypto_alt avg `-0.0582` n `230`; crypto_major avg `-0.0476` n `8`; equity avg `-0.0364` n `113`; fx avg `-0.0019` n `6`; index avg `0.01` n `25`; metal avg `0.0386` n `20`; unknown avg `-0.0135` n `786`
- 1h: commodity avg `0.0527` n `12`; crypto_alt avg `-0.0495` n `230`; crypto_major avg `0.0095` n `8`; equity avg `-0.0911` n `113`; fx avg `0.0105` n `6`; index avg `-0.0114` n `25`; metal avg `0.0084` n `20`; unknown avg `-0.0169` n `786`
- 4h: commodity avg `-0.0548` n `12`; crypto_alt avg `-0.0491` n `230`; crypto_major avg `0.4353` n `8`; equity avg `0.4101` n `113`; fx avg `-0.0362` n `6`; index avg `0.071` n `25`; metal avg `0.1805` n `20`; unknown avg `-0.1224` n `786`
- 24h: commodity avg `0.3588` n `12`; crypto_alt avg `-1.1553` n `230`; crypto_major avg `0.6913` n `8`; equity avg `1.9585` n `113`; fx avg `0.0554` n `6`; index avg `0.1487` n `25`; metal avg `0.1426` n `20`; unknown avg `-0.2316` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2448`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2338`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
