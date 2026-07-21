# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T20:37:28.836577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0405` n `12`; crypto_alt avg `0.0458` n `230`; crypto_major avg `0.1229` n `8`; equity avg `0.0977` n `98`; fx avg `0.0071` n `6`; index avg `0.003` n `25`; metal avg `0.017` n `20`; unknown avg `0.0456` n `771`
- 1h: commodity avg `-0.0421` n `12`; crypto_alt avg `0.033` n `230`; crypto_major avg `-0.0889` n `8`; equity avg `0.4683` n `98`; fx avg `0.0115` n `6`; index avg `0.0027` n `25`; metal avg `0.0083` n `20`; unknown avg `0.0957` n `771`
- 4h: commodity avg `0.0557` n `12`; crypto_alt avg `0.0076` n `230`; crypto_major avg `-0.3296` n `8`; equity avg `0.4621` n `98`; fx avg `0.0569` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.2242` n `771`
- 24h: commodity avg `0.4301` n `12`; crypto_alt avg `0.6644` n `230`; crypto_major avg `0.5406` n `8`; equity avg `4.3595` n `98`; fx avg `0.0749` n `6`; index avg `0.6366` n `25`; metal avg `0.7474` n `20`; unknown avg `0.3067` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
