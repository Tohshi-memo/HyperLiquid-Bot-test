# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T04:52:30.914988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0492` n `12`; crypto_alt avg `-0.119` n `230`; crypto_major avg `-0.1347` n `8`; equity avg `-0.0543` n `98`; fx avg `-0.001` n `6`; index avg `-0.0246` n `25`; metal avg `-0.0629` n `20`; unknown avg `0.0093` n `773`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `0.1388` n `230`; crypto_major avg `-0.0224` n `8`; equity avg `-0.0252` n `98`; fx avg `0.0094` n `6`; index avg `0.0259` n `25`; metal avg `-0.0308` n `20`; unknown avg `-0.1754` n `773`
- 4h: commodity avg `0.0901` n `12`; crypto_alt avg `-0.5799` n `230`; crypto_major avg `-0.6467` n `8`; equity avg `-0.3886` n `98`; fx avg `-0.0285` n `6`; index avg `-0.0548` n `25`; metal avg `0.0527` n `20`; unknown avg `0.4483` n `773`
- 24h: commodity avg `0.7386` n `12`; crypto_alt avg `-0.7142` n `230`; crypto_major avg `-0.9038` n `8`; equity avg `-0.3743` n `98`; fx avg `-0.1493` n `6`; index avg `-0.0061` n `25`; metal avg `-0.0595` n `20`; unknown avg `1.5772` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0797`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
