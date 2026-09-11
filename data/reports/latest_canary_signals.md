# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T01:07:34.193436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1594` n `12`; crypto_alt avg `0.381` n `233`; crypto_major avg `0.332` n `8`; equity avg `0.1322` n `136`; fx avg `-0.0204` n `6`; index avg `0.0275` n `26`; metal avg `0.0222` n `20`; unknown avg `0.3488` n `794`
- 1h: commodity avg `-0.0922` n `12`; crypto_alt avg `0.4488` n `233`; crypto_major avg `0.35` n `8`; equity avg `0.2725` n `136`; fx avg `-0.0096` n `6`; index avg `0.0616` n `26`; metal avg `0.0743` n `20`; unknown avg `0.7153` n `788`
- 4h: commodity avg `-0.2783` n `12`; crypto_alt avg `-0.6443` n `233`; crypto_major avg `-0.5924` n `8`; equity avg `0.0101` n `136`; fx avg `-0.0195` n `6`; index avg `0.0353` n `26`; metal avg `0.0633` n `20`; unknown avg `0.9362` n `750`
- 24h: commodity avg `0.9929` n `12`; crypto_alt avg `-1.8998` n `233`; crypto_major avg `-2.1469` n `8`; equity avg `-1.5839` n `136`; fx avg `0.1166` n `6`; index avg `-0.2374` n `26`; metal avg `-1.2128` n `20`; unknown avg `-0.6837` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
