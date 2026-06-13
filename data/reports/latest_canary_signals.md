# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T22:37:27.816210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1109` n `12`; crypto_alt avg `-0.1018` n `228`; crypto_major avg `-0.0402` n `8`; equity avg `0.0213` n `74`; fx avg `-0.0157` n `6`; index avg `-0.009` n `23`; metal avg `0.0043` n `18`; unknown avg `3.1248` n `645`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `0.4416` n `228`; crypto_major avg `0.2796` n `8`; equity avg `0.0612` n `74`; fx avg `-0.0434` n `6`; index avg `-0.1172` n `23`; metal avg `-0.6917` n `18`; unknown avg `0.858` n `644`
- 4h: commodity avg `0.2382` n `12`; crypto_alt avg `0.2734` n `228`; crypto_major avg `0.398` n `8`; equity avg `0.1502` n `74`; fx avg `-0.0434` n `6`; index avg `0.1171` n `23`; metal avg `0.0358` n `18`; unknown avg `1.5792` n `644`
- 24h: commodity avg `-0.4749` n `12`; crypto_alt avg `2.6556` n `228`; crypto_major avg `1.4171` n `8`; equity avg `0.4744` n `74`; fx avg `0.0402` n `6`; index avg `0.5465` n `23`; metal avg `0.3772` n `18`; unknown avg `0.1143` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
