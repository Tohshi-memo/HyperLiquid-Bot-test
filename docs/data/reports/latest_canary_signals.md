# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T16:22:42.140171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1594` n `12`; crypto_alt avg `-0.3856` n `228`; crypto_major avg `-0.2956` n `8`; equity avg `-0.0725` n `74`; fx avg `-0.0029` n `6`; index avg `-0.0333` n `23`; metal avg `0.034` n `18`; unknown avg `0.145` n `556`
- 1h: commodity avg `0.4239` n `12`; crypto_alt avg `-0.1312` n `228`; crypto_major avg `-0.2988` n `8`; equity avg `0.1162` n `74`; fx avg `-0.0272` n `6`; index avg `0.0648` n `23`; metal avg `0.1986` n `18`; unknown avg `-0.062` n `556`
- 4h: commodity avg `-0.1353` n `12`; crypto_alt avg `0.4533` n `228`; crypto_major avg `0.0373` n `8`; equity avg `0.3798` n `74`; fx avg `-0.084` n `6`; index avg `0.2067` n `23`; metal avg `0.9291` n `18`; unknown avg `0.5207` n `556`
- 24h: commodity avg `-0.6281` n `12`; crypto_alt avg `-0.0905` n `228`; crypto_major avg `-0.5069` n `8`; equity avg `-0.2224` n `74`; fx avg `-0.0473` n `6`; index avg `0.0245` n `23`; metal avg `-0.4781` n `18`; unknown avg `7.2284` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
