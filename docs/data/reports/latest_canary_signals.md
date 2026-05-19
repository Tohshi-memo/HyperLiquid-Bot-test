# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T07:37:15.725295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0297` n `12`; crypto_alt avg `0.0788` n `228`; crypto_major avg `0.0236` n `8`; equity avg `-0.0095` n `66`; fx avg `0.0182` n `6`; index avg `-0.0189` n `23`; metal avg `-0.0357` n `18`; unknown avg `-0.1006` n `383`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `0.1123` n `228`; crypto_major avg `0.2956` n `8`; equity avg `0.3155` n `66`; fx avg `-0.0077` n `6`; index avg `0.0922` n `23`; metal avg `-0.2035` n `18`; unknown avg `0.1802` n `383`
- 4h: commodity avg `0.3568` n `12`; crypto_alt avg `0.3626` n `228`; crypto_major avg `0.3405` n `8`; equity avg `0.145` n `66`; fx avg `0.031` n `6`; index avg `-0.0015` n `23`; metal avg `-0.1909` n `18`; unknown avg `0.451` n `363`
- 24h: commodity avg `0.8853` n `12`; crypto_alt avg `2.0207` n `228`; crypto_major avg `1.2142` n `8`; equity avg `-0.7278` n `66`; fx avg `0.3279` n `6`; index avg `-0.2995` n `23`; metal avg `-0.1945` n `18`; unknown avg `0.836` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
