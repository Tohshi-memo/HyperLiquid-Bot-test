# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T06:22:25.273243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.1866` n `232`; crypto_major avg `-0.1083` n `8`; equity avg `0.0149` n `134`; fx avg `0.0075` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0458` n `792`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `-0.2861` n `232`; crypto_major avg `0.0238` n `8`; equity avg `0.0839` n `134`; fx avg `-0.0015` n `6`; index avg `0.0116` n `26`; metal avg `0.0067` n `20`; unknown avg `32.8081` n `774`
- 4h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0764` n `232`; crypto_major avg `0.564` n `8`; equity avg `0.1272` n `134`; fx avg `0.0021` n `6`; index avg `0.0152` n `26`; metal avg `0.0086` n `20`; unknown avg `464.2944` n `730`
- 24h: commodity avg `0.1633` n `12`; crypto_alt avg `2.1968` n `232`; crypto_major avg `3.0022` n `8`; equity avg `0.4429` n `134`; fx avg `-0.0383` n `6`; index avg `0.0747` n `26`; metal avg `0.0164` n `20`; unknown avg `494.2571` n `676`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
