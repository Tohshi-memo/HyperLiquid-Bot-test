# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T02:52:25.659885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `0.2326` n `228`; crypto_major avg `0.2913` n `8`; equity avg `0.0874` n `74`; fx avg `-0.0007` n `6`; index avg `0.017` n `23`; metal avg `0.0256` n `18`; unknown avg `0.0095` n `516`
- 1h: commodity avg `-0.1104` n `12`; crypto_alt avg `-0.4745` n `228`; crypto_major avg `-0.0932` n `8`; equity avg `-0.0857` n `74`; fx avg `-0.0029` n `6`; index avg `-0.0091` n `23`; metal avg `0.0627` n `18`; unknown avg `-0.2329` n `516`
- 4h: commodity avg `-0.1145` n `12`; crypto_alt avg `1.9158` n `228`; crypto_major avg `1.6722` n `8`; equity avg `0.6843` n `74`; fx avg `-0.0074` n `6`; index avg `0.1152` n `23`; metal avg `0.3534` n `18`; unknown avg `0.8431` n `515`
- 24h: commodity avg `-0.0186` n `12`; crypto_alt avg `0.7096` n `228`; crypto_major avg `-0.0902` n `8`; equity avg `1.4763` n `74`; fx avg `0.0361` n `6`; index avg `0.649` n `23`; metal avg `0.2083` n `18`; unknown avg `-0.1349` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
