# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T20:22:25.711278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.0115` n `230`; crypto_major avg `-0.0813` n `8`; equity avg `0.1105` n `98`; fx avg `0.0003` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0203` n `20`; unknown avg `0.0789` n `771`
- 1h: commodity avg `0.0078` n `12`; crypto_alt avg `-0.0267` n `230`; crypto_major avg `-0.0476` n `8`; equity avg `0.5267` n `98`; fx avg `0.0103` n `6`; index avg `0.0002` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.0211` n `771`
- 4h: commodity avg `0.1006` n `12`; crypto_alt avg `-0.0922` n `230`; crypto_major avg `-0.4553` n `8`; equity avg `0.3613` n `98`; fx avg `0.0479` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0609` n `20`; unknown avg `-0.2621` n `771`
- 24h: commodity avg `0.4838` n `12`; crypto_alt avg `0.783` n `230`; crypto_major avg `0.6061` n `8`; equity avg `4.2846` n `98`; fx avg `0.0692` n `6`; index avg `0.644` n `25`; metal avg `0.7449` n `20`; unknown avg `0.3135` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.086`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
