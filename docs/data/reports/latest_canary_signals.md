# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T10:07:18.026568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0767` n `12`; crypto_alt avg `0.0161` n `228`; crypto_major avg `-0.0353` n `8`; equity avg `-0.0528` n `67`; fx avg `-0.0039` n `6`; index avg `-0.0423` n `23`; metal avg `0.0012` n `18`; unknown avg `-0.1156` n `419`
- 1h: commodity avg `0.0855` n `12`; crypto_alt avg `0.4433` n `228`; crypto_major avg `0.328` n `8`; equity avg `-0.0927` n `67`; fx avg `-0.0104` n `6`; index avg `-0.0591` n `23`; metal avg `0.0292` n `18`; unknown avg `-0.0017` n `419`
- 4h: commodity avg `-0.299` n `12`; crypto_alt avg `0.5272` n `228`; crypto_major avg `0.503` n `8`; equity avg `0.2746` n `67`; fx avg `0.0074` n `6`; index avg `0.0611` n `23`; metal avg `0.3206` n `18`; unknown avg `0.2035` n `419`
- 24h: commodity avg `0.418` n `12`; crypto_alt avg `-4.2996` n `228`; crypto_major avg `-3.5052` n `8`; equity avg `-1.6292` n `67`; fx avg `-0.1011` n `6`; index avg `-1.0824` n `23`; metal avg `-1.719` n `18`; unknown avg `-1.5746` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
