# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T06:36:11.943927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `12`; crypto_alt avg `0.0992` n `228`; crypto_major avg `0.0684` n `8`; equity avg `0.0022` n `88`; fx avg `-0.0037` n `6`; index avg `0.0113` n `23`; metal avg `0.0071` n `20`; unknown avg `-0.1435` n `764`
- 1h: commodity avg `0.0381` n `12`; crypto_alt avg `-0.1777` n `228`; crypto_major avg `-0.0473` n `8`; equity avg `0.0102` n `88`; fx avg `0.0131` n `6`; index avg `-0.0161` n `23`; metal avg `0.0377` n `20`; unknown avg `-0.2767` n `732`
- 4h: commodity avg `-0.1835` n `12`; crypto_alt avg `-0.1387` n `228`; crypto_major avg `-0.3352` n `8`; equity avg `-0.0064` n `88`; fx avg `-0.0031` n `6`; index avg `-0.0004` n `23`; metal avg `0.0077` n `20`; unknown avg `0.5053` n `706`
- 24h: commodity avg `0.3139` n `12`; crypto_alt avg `-0.7875` n `228`; crypto_major avg `-1.5323` n `8`; equity avg `-0.0791` n `88`; fx avg `-0.0188` n `6`; index avg `-0.1278` n `23`; metal avg `-0.0464` n `20`; unknown avg `15.979` n `682`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
