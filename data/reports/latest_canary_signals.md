# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T20:52:26.491718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.0205` n `230`; crypto_major avg `-0.015` n `8`; equity avg `-0.0268` n `98`; fx avg `0.0044` n `6`; index avg `-0.0273` n `25`; metal avg `-0.0275` n `20`; unknown avg `0.0579` n `773`
- 1h: commodity avg `-0.015` n `12`; crypto_alt avg `0.206` n `230`; crypto_major avg `0.103` n `8`; equity avg `0.2103` n `98`; fx avg `0.0092` n `6`; index avg `0.0137` n `25`; metal avg `0.0066` n `20`; unknown avg `0.0698` n `773`
- 4h: commodity avg `0.0886` n `12`; crypto_alt avg `-0.48` n `230`; crypto_major avg `-0.4307` n `8`; equity avg `-0.33` n `98`; fx avg `0.019` n `6`; index avg `-0.0548` n `25`; metal avg `-0.0932` n `20`; unknown avg `0.1844` n `773`
- 24h: commodity avg `0.4836` n `12`; crypto_alt avg `-0.3683` n `230`; crypto_major avg `-0.6225` n `8`; equity avg `-0.8673` n `98`; fx avg `-0.0556` n `6`; index avg `-0.1157` n `25`; metal avg `0.2776` n `20`; unknown avg `0.8848` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0869`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
