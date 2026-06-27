# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T08:22:24.277327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.1035` n `228`; crypto_major avg `-0.1993` n `8`; equity avg `-0.0123` n `88`; fx avg `0.0213` n `6`; index avg `-0.0066` n `23`; metal avg `-0.0051` n `20`; unknown avg `0.0227` n `764`
- 1h: commodity avg `0.0342` n `12`; crypto_alt avg `-0.2235` n `228`; crypto_major avg `-0.0941` n `8`; equity avg `0.0591` n `88`; fx avg `0.0036` n `6`; index avg `-0.0008` n `23`; metal avg `-0.0095` n `20`; unknown avg `0.0114` n `748`
- 4h: commodity avg `0.0489` n `12`; crypto_alt avg `-0.5294` n `228`; crypto_major avg `-0.375` n `8`; equity avg `0.1439` n `88`; fx avg `0.0248` n `6`; index avg `-0.0032` n `23`; metal avg `-0.0304` n `20`; unknown avg `-0.2542` n `716`
- 24h: commodity avg `0.0381` n `12`; crypto_alt avg `0.8555` n `228`; crypto_major avg `0.5954` n `8`; equity avg `1.4807` n `87`; fx avg `0.0532` n `6`; index avg `0.019` n `23`; metal avg `0.6183` n `20`; unknown avg `-0.1751` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2049`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
