# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T19:37:38.807902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `-0.0137` n `230`; crypto_major avg `0.1646` n `8`; equity avg `0.157` n `98`; fx avg `0.0058` n `6`; index avg `0.0006` n `25`; metal avg `-0.0216` n `20`; unknown avg `-0.0068` n `771`
- 1h: commodity avg `0.0866` n `12`; crypto_alt avg `-0.0358` n `230`; crypto_major avg `0.0848` n `8`; equity avg `-0.0191` n `98`; fx avg `0.0191` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0188` n `20`; unknown avg `-0.0693` n `771`
- 4h: commodity avg `0.0232` n `12`; crypto_alt avg `-0.0893` n `230`; crypto_major avg `-0.1753` n `8`; equity avg `0.258` n `98`; fx avg `0.0381` n `6`; index avg `0.032` n `25`; metal avg `-0.0488` n `20`; unknown avg `-0.0208` n `771`
- 24h: commodity avg `0.448` n `12`; crypto_alt avg `1.0621` n `230`; crypto_major avg `1.1244` n `8`; equity avg `3.6781` n `98`; fx avg `0.0544` n `6`; index avg `0.5783` n `25`; metal avg `0.733` n `20`; unknown avg `0.3309` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.088`, n `666`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0518`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
