# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T07:22:18.787419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `0.0533` n `228`; crypto_major avg `0.2303` n `8`; equity avg `0.0952` n `66`; fx avg `0.0067` n `6`; index avg `0.0255` n `23`; metal avg `-0.0996` n `18`; unknown avg `0.1576` n `383`
- 1h: commodity avg `0.2154` n `12`; crypto_alt avg `0.0554` n `228`; crypto_major avg `0.2662` n `8`; equity avg `0.3512` n `66`; fx avg `-0.0358` n `6`; index avg `0.1138` n `23`; metal avg `-0.286` n `18`; unknown avg `0.3094` n `383`
- 4h: commodity avg `0.2897` n `12`; crypto_alt avg `0.4655` n `228`; crypto_major avg `0.5077` n `8`; equity avg `0.3836` n `66`; fx avg `0.0069` n `6`; index avg `0.121` n `23`; metal avg `-0.2287` n `18`; unknown avg `0.4943` n `363`
- 24h: commodity avg `0.6662` n `12`; crypto_alt avg `2.1404` n `228`; crypto_major avg `1.4365` n `8`; equity avg `-0.5232` n `66`; fx avg `0.2784` n `6`; index avg `-0.1909` n `23`; metal avg `0.1887` n `18`; unknown avg `1.1084` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
