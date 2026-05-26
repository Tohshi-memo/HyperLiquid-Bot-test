# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T08:07:19.872353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.083` n `12`; crypto_alt avg `0.0446` n `228`; crypto_major avg `-0.0818` n `8`; equity avg `0.0475` n `67`; fx avg `0.006` n `6`; index avg `-0.007` n `23`; metal avg `0.027` n `18`; unknown avg `-0.0072` n `417`
- 1h: commodity avg `0.2477` n `12`; crypto_alt avg `-0.12` n `228`; crypto_major avg `-0.2408` n `8`; equity avg `-0.1168` n `67`; fx avg `0.0284` n `6`; index avg `-0.0541` n `23`; metal avg `-0.0497` n `18`; unknown avg `-0.0147` n `417`
- 4h: commodity avg `0.4673` n `12`; crypto_alt avg `0.6382` n `228`; crypto_major avg `0.1943` n `8`; equity avg `-0.1776` n `67`; fx avg `-0.0272` n `6`; index avg `-0.0558` n `23`; metal avg `-0.2114` n `18`; unknown avg `0.3517` n `397`
- 24h: commodity avg `0.7191` n `12`; crypto_alt avg `-0.7537` n `228`; crypto_major avg `-1.5954` n `8`; equity avg `-0.7299` n `67`; fx avg `-0.1143` n `6`; index avg `-0.0829` n `23`; metal avg `-0.4705` n `18`; unknown avg `-0.1135` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
