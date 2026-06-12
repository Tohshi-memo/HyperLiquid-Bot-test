# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T04:07:31.421167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2279` n `12`; crypto_alt avg `-0.1195` n `228`; crypto_major avg `-0.0954` n `8`; equity avg `-0.1004` n `74`; fx avg `0.0104` n `6`; index avg `0.0154` n `23`; metal avg `-0.1511` n `18`; unknown avg `-0.1074` n `557`
- 1h: commodity avg `-0.4245` n `12`; crypto_alt avg `-0.2082` n `228`; crypto_major avg `-0.2409` n `8`; equity avg `-0.0998` n `74`; fx avg `0.0105` n `6`; index avg `0.0498` n `23`; metal avg `-0.1004` n `18`; unknown avg `-0.0452` n `557`
- 4h: commodity avg `-0.2453` n `12`; crypto_alt avg `-0.2656` n `228`; crypto_major avg `-0.3321` n `8`; equity avg `-0.2341` n `74`; fx avg `0.0` n `6`; index avg `-0.2114` n `23`; metal avg `-0.2238` n `18`; unknown avg `-0.2853` n `556`
- 24h: commodity avg `-2.7615` n `12`; crypto_alt avg `1.8569` n `228`; crypto_major avg `2.2847` n `8`; equity avg `3.6857` n `74`; fx avg `0.039` n `6`; index avg `1.9463` n `23`; metal avg `3.1951` n `18`; unknown avg `2.2574` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
