# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T06:37:31.278156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0229` n `12`; crypto_alt avg `0.4374` n `228`; crypto_major avg `0.2162` n `8`; equity avg `0.0406` n `74`; fx avg `-0.001` n `6`; index avg `-0.0498` n `23`; metal avg `0.0093` n `18`; unknown avg `0.0494` n `643`
- 1h: commodity avg `-0.0617` n `12`; crypto_alt avg `0.4942` n `228`; crypto_major avg `0.385` n `8`; equity avg `-0.0078` n `74`; fx avg `-0.0214` n `6`; index avg `-0.051` n `23`; metal avg `0.011` n `18`; unknown avg `0.274` n `627`
- 4h: commodity avg `-0.1175` n `12`; crypto_alt avg `-0.0798` n `228`; crypto_major avg `-0.41` n `8`; equity avg `-0.4427` n `74`; fx avg `0.0262` n `6`; index avg `-0.0832` n `23`; metal avg `-0.0692` n `18`; unknown avg `-0.4243` n `619`
- 24h: commodity avg `-0.5979` n `12`; crypto_alt avg `1.5641` n `228`; crypto_major avg `1.1078` n `8`; equity avg `-0.1287` n `74`; fx avg `0.003` n `6`; index avg `0.957` n `23`; metal avg `0.7862` n `18`; unknown avg `36.6451` n `507`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
