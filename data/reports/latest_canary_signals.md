# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T17:13:32.964161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `-0.0141` n `228`; crypto_major avg `0.0857` n `8`; equity avg `0.0049` n `74`; fx avg `-0.001` n `6`; index avg `0.0151` n `23`; metal avg `-0.0547` n `18`; unknown avg `-0.0223` n `643`
- 1h: commodity avg `0.0961` n `12`; crypto_alt avg `0.482` n `228`; crypto_major avg `0.7733` n `8`; equity avg `0.8959` n `74`; fx avg `-0.0177` n `6`; index avg `0.3182` n `23`; metal avg `0.2229` n `18`; unknown avg `-0.1315` n `643`
- 4h: commodity avg `-0.0209` n `12`; crypto_alt avg `-0.1321` n `228`; crypto_major avg `0.7644` n `8`; equity avg `0.2747` n `74`; fx avg `-0.006` n `6`; index avg `0.55` n `23`; metal avg `0.4778` n `18`; unknown avg `26.4695` n `643`
- 24h: commodity avg `-1.9697` n `12`; crypto_alt avg `2.1268` n `228`; crypto_major avg `3.2574` n `8`; equity avg `2.7176` n `74`; fx avg `0.0952` n `6`; index avg `2.023` n `23`; metal avg `3.1736` n `18`; unknown avg `43.7554` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
