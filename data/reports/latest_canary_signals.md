# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T22:52:25.953388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.0461` n `229`; crypto_major avg `-0.0211` n `8`; equity avg `0.0137` n `88`; fx avg `-0.0272` n `6`; index avg `0.0029` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.0563` n `765`
- 1h: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.2558` n `229`; crypto_major avg `-0.2364` n `8`; equity avg `-0.054` n `88`; fx avg `-0.0216` n `6`; index avg `-0.0029` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.1929` n `765`
- 4h: commodity avg `-0.0564` n `12`; crypto_alt avg `0.5487` n `229`; crypto_major avg `0.5477` n `8`; equity avg `-0.0497` n `88`; fx avg `-0.0338` n `6`; index avg `-0.0459` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.2876` n `765`
- 24h: commodity avg `0.1411` n `12`; crypto_alt avg `3.1894` n `229`; crypto_major avg `3.4017` n `8`; equity avg `1.7274` n `88`; fx avg `-0.0902` n `6`; index avg `0.4421` n `25`; metal avg `0.5348` n `20`; unknown avg `4.9392` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
