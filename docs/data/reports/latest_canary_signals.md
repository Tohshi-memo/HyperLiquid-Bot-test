# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T16:22:34.196926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `-0.1096` n `230`; crypto_major avg `-0.184` n `8`; equity avg `-0.1034` n `98`; fx avg `-0.004` n `6`; index avg `0.004` n `25`; metal avg `-0.0695` n `20`; unknown avg `0.0964` n `773`
- 1h: commodity avg `-0.1039` n `12`; crypto_alt avg `-0.201` n `230`; crypto_major avg `-0.3314` n `8`; equity avg `-0.119` n `98`; fx avg `-0.0037` n `6`; index avg `0.0341` n `25`; metal avg `-0.0589` n `20`; unknown avg `0.1443` n `773`
- 4h: commodity avg `-0.1088` n `12`; crypto_alt avg `0.4062` n `230`; crypto_major avg `0.4552` n `8`; equity avg `1.6234` n `98`; fx avg `-0.0262` n `6`; index avg `0.3273` n `25`; metal avg `0.0342` n `20`; unknown avg `9.645` n `773`
- 24h: commodity avg `0.4509` n `12`; crypto_alt avg `-0.2628` n `230`; crypto_major avg `-0.9576` n `8`; equity avg `0.0682` n `98`; fx avg `-0.0226` n `6`; index avg `-0.0388` n `25`; metal avg `0.3459` n `20`; unknown avg `0.9622` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1075`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0929`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0738`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal
