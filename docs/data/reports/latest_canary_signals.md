# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T02:07:34.335416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0395` n `12`; crypto_alt avg `-0.0475` n `230`; crypto_major avg `-0.045` n `8`; equity avg `-0.0928` n `100`; fx avg `0.0012` n `6`; index avg `-0.0353` n `25`; metal avg `-0.0618` n `20`; unknown avg `-0.0509` n `772`
- 1h: commodity avg `0.0487` n `12`; crypto_alt avg `0.2226` n `230`; crypto_major avg `0.0872` n `8`; equity avg `-0.1133` n `100`; fx avg `-0.0273` n `6`; index avg `-0.0653` n `25`; metal avg `-0.0371` n `20`; unknown avg `0.0461` n `772`
- 4h: commodity avg `-0.0759` n `12`; crypto_alt avg `-0.043` n `230`; crypto_major avg `-0.125` n `8`; equity avg `-0.4007` n `100`; fx avg `-0.1025` n `6`; index avg `-0.1587` n `25`; metal avg `-0.0878` n `20`; unknown avg `-0.4918` n `772`
- 24h: commodity avg `0.5352` n `12`; crypto_alt avg `-1.3122` n `230`; crypto_major avg `-1.9821` n `8`; equity avg `-1.797` n `99`; fx avg `-0.0938` n `6`; index avg `-0.5067` n `25`; metal avg `-0.8827` n `20`; unknown avg `-0.3565` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0915`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.085`, n `666`, weak_sample_signal
