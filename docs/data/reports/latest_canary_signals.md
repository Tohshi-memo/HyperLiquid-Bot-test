# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T22:52:30.808429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0619` n `13`; crypto_alt avg `-0.0548` n `236`; crypto_major avg `-0.065` n `8`; equity avg `-0.0717` n `151`; fx avg `0.0029` n `6`; index avg `-0.0182` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.1685` n `1136`
- 1h: commodity avg `-0.0293` n `13`; crypto_alt avg `0.0312` n `236`; crypto_major avg `-0.0277` n `8`; equity avg `-0.1166` n `151`; fx avg `0.0057` n `6`; index avg `-0.0389` n `26`; metal avg `-0.0195` n `20`; unknown avg `-0.2695` n `1102`
- 4h: commodity avg `-0.1417` n `13`; crypto_alt avg `0.0642` n `236`; crypto_major avg `0.0806` n `8`; equity avg `0.9579` n `151`; fx avg `-0.0086` n `6`; index avg `0.0832` n `26`; metal avg `0.0592` n `20`; unknown avg `0.0869` n `1020`
- 24h: commodity avg `-0.2907` n `13`; crypto_alt avg `0.5187` n `236`; crypto_major avg `0.6674` n `8`; equity avg `1.0198` n `151`; fx avg `0.1507` n `6`; index avg `-0.0009` n `26`; metal avg `0.4439` n `20`; unknown avg `24.9188` n `910`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0963`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0767`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0752`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0717`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0483`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
