# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T13:52:24.206985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `0.8338` n `232`; crypto_major avg `0.9126` n `8`; equity avg `0.1117` n `133`; fx avg `-0.0264` n `6`; index avg `-0.0116` n `26`; metal avg `0.084` n `20`; unknown avg `0.7935` n `791`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.7696` n `232`; crypto_major avg `0.9102` n `8`; equity avg `0.2597` n `133`; fx avg `-0.1158` n `6`; index avg `0.0379` n `26`; metal avg `0.3804` n `20`; unknown avg `0.6159` n `789`
- 4h: commodity avg `-0.1432` n `12`; crypto_alt avg `0.2718` n `232`; crypto_major avg `0.7194` n `8`; equity avg `0.7504` n `133`; fx avg `-0.1707` n `6`; index avg `0.144` n `26`; metal avg `0.666` n `20`; unknown avg `0.9933` n `789`
- 24h: commodity avg `0.4963` n `12`; crypto_alt avg `-0.7525` n `232`; crypto_major avg `-1.3707` n `8`; equity avg `-0.2977` n `132`; fx avg `-0.3672` n `6`; index avg `-0.119` n `26`; metal avg `0.2034` n `20`; unknown avg `0.1194` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
