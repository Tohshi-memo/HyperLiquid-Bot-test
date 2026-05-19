# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T02:52:15.618202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.0238` n `228`; crypto_major avg `-0.0417` n `8`; equity avg `0.0919` n `66`; fx avg `-0.0079` n `6`; index avg `0.0525` n `23`; metal avg `-0.0543` n `18`; unknown avg `-0.1839` n `383`
- 1h: commodity avg `0.0974` n `12`; crypto_alt avg `-0.2384` n `228`; crypto_major avg `-0.0992` n `8`; equity avg `-0.1644` n `66`; fx avg `0.0017` n `6`; index avg `-0.1561` n `23`; metal avg `-0.635` n `18`; unknown avg `-0.3066` n `383`
- 4h: commodity avg `0.2281` n `12`; crypto_alt avg `-0.0533` n `228`; crypto_major avg `-0.2017` n `8`; equity avg `-0.5901` n `66`; fx avg `0.1316` n `6`; index avg `-0.4703` n `23`; metal avg `-1.0899` n `18`; unknown avg `-0.5084` n `383`
- 24h: commodity avg `0.2066` n `12`; crypto_alt avg `0.5587` n `228`; crypto_major avg `0.1778` n `8`; equity avg `-0.8892` n `66`; fx avg `0.2239` n `6`; index avg `-0.2219` n `23`; metal avg `0.6978` n `18`; unknown avg `0.1745` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
