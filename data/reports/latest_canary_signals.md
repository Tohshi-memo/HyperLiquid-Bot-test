# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T10:37:30.343928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.0529` n `230`; crypto_major avg `0.0115` n `8`; equity avg `-0.0217` n `98`; fx avg `-0.0099` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0186` n `20`; unknown avg `-0.0028` n `773`
- 1h: commodity avg `-0.1208` n `12`; crypto_alt avg `0.2686` n `230`; crypto_major avg `0.3054` n `8`; equity avg `0.1344` n `98`; fx avg `-0.0094` n `6`; index avg `0.039` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.0277` n `773`
- 4h: commodity avg `0.1133` n `12`; crypto_alt avg `0.4155` n `230`; crypto_major avg `0.3774` n `8`; equity avg `0.1587` n `98`; fx avg `0.0024` n `6`; index avg `0.0307` n `25`; metal avg `0.0502` n `20`; unknown avg `0.0505` n `772`
- 24h: commodity avg `0.6366` n `12`; crypto_alt avg `-0.6121` n `230`; crypto_major avg `-1.368` n `8`; equity avg `0.4969` n `98`; fx avg `-0.0207` n `6`; index avg `-0.009` n `25`; metal avg `0.2681` n `20`; unknown avg `0.1073` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.103`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0785`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0694`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0681`, n `666`, weak_sample_signal
