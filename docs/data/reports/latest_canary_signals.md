# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T17:07:31.196134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0589` n `12`; crypto_alt avg `0.2093` n `228`; crypto_major avg `0.2483` n `8`; equity avg `0.3219` n `74`; fx avg `-0.0017` n `6`; index avg `0.1313` n `23`; metal avg `0.1051` n `18`; unknown avg `-0.0287` n `643`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `0.7069` n `228`; crypto_major avg `0.9361` n `8`; equity avg `1.2179` n `74`; fx avg `-0.0183` n `6`; index avg `0.435` n `23`; metal avg `0.3833` n `18`; unknown avg `-0.1115` n `643`
- 4h: commodity avg `-0.1222` n `12`; crypto_alt avg `0.0909` n `228`; crypto_major avg `0.9283` n `8`; equity avg `0.5914` n `74`; fx avg `-0.0066` n `6`; index avg `0.6671` n `23`; metal avg `0.6384` n `18`; unknown avg `27.0517` n `643`
- 24h: commodity avg `-2.0657` n `12`; crypto_alt avg `2.3554` n `228`; crypto_major avg `3.4217` n `8`; equity avg `3.0455` n `74`; fx avg `0.0947` n `6`; index avg `2.1426` n `23`; metal avg `3.3395` n `18`; unknown avg `44.6202` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
