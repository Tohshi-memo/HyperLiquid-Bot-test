# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T23:07:35.126436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `0.291` n `232`; crypto_major avg `0.2651` n `8`; equity avg `-0.04` n `134`; fx avg `-0.0065` n `6`; index avg `-0.0122` n `26`; metal avg `0.0195` n `20`; unknown avg `1.0088` n `795`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `-0.2903` n `232`; crypto_major avg `0.0084` n `8`; equity avg `-0.188` n `134`; fx avg `-0.0307` n `6`; index avg `-0.0466` n `26`; metal avg `-0.0127` n `20`; unknown avg `12.8615` n `795`
- 4h: commodity avg `0.0224` n `12`; crypto_alt avg `0.1169` n `232`; crypto_major avg `0.143` n `8`; equity avg `-0.1374` n `134`; fx avg `-0.0271` n `6`; index avg `-0.0556` n `26`; metal avg `0.0067` n `20`; unknown avg `8.0465` n `752`
- 24h: commodity avg `0.238` n `12`; crypto_alt avg `-0.3663` n `232`; crypto_major avg `-1.3546` n `8`; equity avg `0.3096` n `134`; fx avg `-0.1758` n `6`; index avg `0.0522` n `26`; metal avg `0.0562` n `20`; unknown avg `7945.7398` n `642`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
