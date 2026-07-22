# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T04:52:24.377276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.0234` n `230`; crypto_major avg `0.0037` n `8`; equity avg `-0.1327` n `98`; fx avg `0.0056` n `6`; index avg `-0.0273` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.0063` n `771`
- 1h: commodity avg `0.01` n `12`; crypto_alt avg `-0.0061` n `230`; crypto_major avg `0.0248` n `8`; equity avg `-0.13` n `98`; fx avg `-0.0009` n `6`; index avg `-0.0229` n `25`; metal avg `-0.0619` n `20`; unknown avg `-0.2432` n `771`
- 4h: commodity avg `0.0966` n `12`; crypto_alt avg `-0.3754` n `230`; crypto_major avg `-0.435` n `8`; equity avg `-0.7729` n `98`; fx avg `0.0361` n `6`; index avg `-0.0878` n `25`; metal avg `0.2699` n `20`; unknown avg `-0.4586` n `771`
- 24h: commodity avg `0.62` n `12`; crypto_alt avg `-0.0012` n `230`; crypto_major avg `-0.0133` n `8`; equity avg `2.1735` n `98`; fx avg `0.0867` n `6`; index avg `0.2639` n `25`; metal avg `0.743` n `20`; unknown avg `0.2785` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0966`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0622`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0534`, n `666`, weak_sample_signal
