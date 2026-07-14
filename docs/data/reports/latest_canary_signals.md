# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T17:52:26.293580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0424` n `12`; crypto_alt avg `0.1026` n `230`; crypto_major avg `0.2142` n `8`; equity avg `0.104` n `92`; fx avg `-0.0085` n `6`; index avg `0.0009` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.1137` n `767`
- 1h: commodity avg `-0.1005` n `12`; crypto_alt avg `-0.2607` n `230`; crypto_major avg `-0.1414` n `8`; equity avg `0.0485` n `92`; fx avg `-0.0141` n `6`; index avg `0.0073` n `25`; metal avg `0.0038` n `20`; unknown avg `0.2133` n `766`
- 4h: commodity avg `-0.2198` n `12`; crypto_alt avg `0.1146` n `230`; crypto_major avg `0.5014` n `8`; equity avg `0.263` n `92`; fx avg `-0.0386` n `6`; index avg `0.0662` n `25`; metal avg `-0.1069` n `20`; unknown avg `-0.331` n `758`
- 24h: commodity avg `0.2517` n `12`; crypto_alt avg `1.9355` n `230`; crypto_major avg `3.4302` n `8`; equity avg `1.3981` n `92`; fx avg `-0.0285` n `6`; index avg `0.3794` n `25`; metal avg `0.6936` n `20`; unknown avg `-0.0443` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
