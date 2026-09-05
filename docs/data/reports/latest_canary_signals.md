# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T20:37:24.261566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `12`; crypto_alt avg `0.0142` n `232`; crypto_major avg `0.0387` n `8`; equity avg `0.0` n `134`; fx avg `0.0007` n `6`; index avg `0.0161` n `26`; metal avg `0.0001` n `20`; unknown avg `18.4234` n `794`
- 1h: commodity avg `0.0176` n `12`; crypto_alt avg `0.0427` n `232`; crypto_major avg `-0.1892` n `8`; equity avg `0.0037` n `134`; fx avg `-0.0024` n `6`; index avg `-0.009` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.8562` n `774`
- 4h: commodity avg `0.05` n `12`; crypto_alt avg `0.473` n `232`; crypto_major avg `0.4304` n `8`; equity avg `0.0318` n `134`; fx avg `-0.0155` n `6`; index avg `0.0337` n `26`; metal avg `0.0144` n `20`; unknown avg `1.291` n `774`
- 24h: commodity avg `0.1198` n `12`; crypto_alt avg `2.7262` n `232`; crypto_major avg `2.2659` n `8`; equity avg `0.2677` n `134`; fx avg `-0.0292` n `6`; index avg `0.0343` n `26`; metal avg `0.0571` n `20`; unknown avg `334.4566` n `662`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
