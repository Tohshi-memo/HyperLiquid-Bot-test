# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T04:07:27.528166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.1396` n `232`; crypto_major avg `-0.2282` n `8`; equity avg `-0.0214` n `134`; fx avg `-0.0263` n `6`; index avg `0.0066` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.08` n `776`
- 1h: commodity avg `0.0261` n `12`; crypto_alt avg `0.2557` n `232`; crypto_major avg `0.2707` n `8`; equity avg `0.0138` n `134`; fx avg `-0.0084` n `6`; index avg `0.0142` n `26`; metal avg `0.0118` n `20`; unknown avg `8.3282` n `760`
- 4h: commodity avg `0.0666` n `12`; crypto_alt avg `0.9118` n `232`; crypto_major avg `0.7468` n `8`; equity avg `0.0788` n `134`; fx avg `-0.0133` n `6`; index avg `0.0079` n `26`; metal avg `-0.0061` n `20`; unknown avg `11.1214` n `754`
- 24h: commodity avg `0.1386` n `12`; crypto_alt avg `3.1818` n `232`; crypto_major avg `3.0272` n `8`; equity avg `0.4936` n `134`; fx avg `-0.0826` n `6`; index avg `0.098` n `26`; metal avg `0.0304` n `20`; unknown avg `1.0973` n `682`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
