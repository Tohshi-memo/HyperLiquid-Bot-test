# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T00:37:16.275303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `0.0479` n `228`; crypto_major avg `-0.0249` n `8`; equity avg `0.0619` n `67`; fx avg `-0.0126` n `6`; index avg `0.0275` n `23`; metal avg `0.06` n `18`; unknown avg `0.1504` n `396`
- 1h: commodity avg `0.111` n `12`; crypto_alt avg `0.3656` n `228`; crypto_major avg `0.0125` n `8`; equity avg `0.1144` n `67`; fx avg `-0.1103` n `6`; index avg `0.0699` n `23`; metal avg `-0.2337` n `18`; unknown avg `0.2782` n `396`
- 4h: commodity avg `-0.7701` n `12`; crypto_alt avg `0.3053` n `228`; crypto_major avg `0.338` n `8`; equity avg `0.0374` n `67`; fx avg `-0.0856` n `6`; index avg `0.0073` n `23`; metal avg `1.3779` n `18`; unknown avg `0.2019` n `396`
- 24h: commodity avg `0.3919` n `12`; crypto_alt avg `-1.3177` n `228`; crypto_major avg `0.3866` n `8`; equity avg `0.4016` n `67`; fx avg `0.005` n `6`; index avg `-0.1181` n `23`; metal avg `0.9945` n `18`; unknown avg `-0.1692` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
