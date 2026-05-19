# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T02:22:20.216140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `0.33` n `228`; crypto_major avg `0.2082` n `8`; equity avg `-0.0142` n `66`; fx avg `0.0103` n `6`; index avg `-0.0144` n `23`; metal avg `-0.0603` n `18`; unknown avg `-0.0358` n `383`
- 1h: commodity avg `-0.1832` n `12`; crypto_alt avg `0.0672` n `228`; crypto_major avg `-0.1966` n `8`; equity avg `-0.0884` n `66`; fx avg `0.0072` n `6`; index avg `-0.1111` n `23`; metal avg `-0.2871` n `18`; unknown avg `-0.5677` n `383`
- 4h: commodity avg `0.1276` n `12`; crypto_alt avg `-0.1691` n `228`; crypto_major avg `-0.5481` n `8`; equity avg `-0.7671` n `66`; fx avg `0.1337` n `6`; index avg `-0.5264` n `23`; metal avg `-0.7906` n `18`; unknown avg `-0.6551` n `383`
- 24h: commodity avg `0.0559` n `12`; crypto_alt avg `0.8474` n `228`; crypto_major avg `-0.0298` n `8`; equity avg `-1.2066` n `66`; fx avg `0.2145` n `6`; index avg `-0.4054` n `23`; metal avg `0.86` n `18`; unknown avg `0.1344` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
