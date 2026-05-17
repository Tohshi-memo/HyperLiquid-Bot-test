# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T12:37:13.495054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `0.1041` n `228`; crypto_major avg `0.1838` n `8`; equity avg `0.14` n `65`; fx avg `0.0006` n `5`; index avg `-0.0066` n `23`; metal avg `0.0029` n `18`; unknown avg `-0.0249` n `383`
- 1h: commodity avg `0.0415` n `12`; crypto_alt avg `0.0959` n `228`; crypto_major avg `0.2557` n `8`; equity avg `0.0908` n `65`; fx avg `-0.017` n `5`; index avg `-0.0549` n `23`; metal avg `0.0101` n `18`; unknown avg `-0.0054` n `383`
- 4h: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.009` n `228`; crypto_major avg `0.6819` n `8`; equity avg `0.3889` n `65`; fx avg `-0.0132` n `5`; index avg `0.0683` n `23`; metal avg `-0.0428` n `18`; unknown avg `0.0143` n `383`
- 24h: commodity avg `1.7745` n `12`; crypto_alt avg `-8.9045` n `228`; crypto_major avg `-2.0185` n `8`; equity avg `-2.5264` n `65`; fx avg `-0.1838` n `5`; index avg `-1.7196` n `23`; metal avg `-5.8533` n `18`; unknown avg `550.127` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
