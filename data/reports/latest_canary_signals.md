# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T04:37:20.838084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `0.51` n `228`; crypto_major avg `0.3746` n `8`; equity avg `0.0092` n `67`; fx avg `-0.0058` n `6`; index avg `-0.027` n `23`; metal avg `-0.1579` n `18`; unknown avg `-0.0221` n `407`
- 1h: commodity avg `0.1202` n `12`; crypto_alt avg `0.5736` n `228`; crypto_major avg `0.2578` n `8`; equity avg `0.031` n `67`; fx avg `-0.0199` n `6`; index avg `0.0131` n `23`; metal avg `-0.3211` n `18`; unknown avg `-0.3647` n `407`
- 4h: commodity avg `0.1776` n `12`; crypto_alt avg `-0.2981` n `228`; crypto_major avg `-0.2941` n `8`; equity avg `-0.2367` n `67`; fx avg `-0.0494` n `6`; index avg `-0.0163` n `23`; metal avg `-0.6431` n `18`; unknown avg `-0.0255` n `407`
- 24h: commodity avg `0.5049` n `12`; crypto_alt avg `0.114` n `228`; crypto_major avg `-0.7839` n `8`; equity avg `-0.3774` n `67`; fx avg `-0.0213` n `6`; index avg `-0.0544` n `23`; metal avg `-0.4813` n `18`; unknown avg `0.0429` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
