# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T23:22:29.921471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `0.0574` n `228`; crypto_major avg `0.1216` n `8`; equity avg `-0.1208` n `74`; fx avg `-0.021` n `6`; index avg `-0.0032` n `23`; metal avg `-0.0051` n `18`; unknown avg `0.4149` n `645`
- 1h: commodity avg `-0.201` n `12`; crypto_alt avg `-0.1772` n `228`; crypto_major avg `0.0601` n `8`; equity avg `0.0349` n `74`; fx avg `-0.0159` n `6`; index avg `-0.0428` n `23`; metal avg `-0.0039` n `18`; unknown avg `3.5956` n `645`
- 4h: commodity avg `0.1906` n `12`; crypto_alt avg `0.3947` n `228`; crypto_major avg `0.6047` n `8`; equity avg `0.162` n `74`; fx avg `-0.0336` n `6`; index avg `0.0539` n `23`; metal avg `0.0214` n `18`; unknown avg `9.5128` n `644`
- 24h: commodity avg `-0.3431` n `12`; crypto_alt avg `2.8394` n `228`; crypto_major avg `1.8148` n `8`; equity avg `0.4377` n `74`; fx avg `0.017` n `6`; index avg `0.478` n `23`; metal avg `0.3088` n `18`; unknown avg `0.7866` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
