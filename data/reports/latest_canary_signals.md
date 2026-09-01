# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T09:22:28.130597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `0.1916` n `232`; crypto_major avg `0.0998` n `8`; equity avg `-0.0344` n `130`; fx avg `0.0092` n `6`; index avg `-0.009` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.1104` n `792`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.5102` n `232`; crypto_major avg `-0.2929` n `8`; equity avg `-0.6416` n `130`; fx avg `0.0155` n `6`; index avg `-0.1533` n `26`; metal avg `-0.2727` n `20`; unknown avg `0.0605` n `790`
- 4h: commodity avg `0.1394` n `12`; crypto_alt avg `-1.0829` n `232`; crypto_major avg `-0.9133` n `8`; equity avg `-1.2415` n `130`; fx avg `0.0215` n `6`; index avg `-0.25` n `26`; metal avg `-0.5086` n `20`; unknown avg `-0.2648` n `770`
- 24h: commodity avg `0.3806` n `12`; crypto_alt avg `0.1405` n `232`; crypto_major avg `-0.1553` n `8`; equity avg `-0.8977` n `130`; fx avg `0.0974` n `6`; index avg `-0.3204` n `26`; metal avg `-0.7359` n `20`; unknown avg `0.0811` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0455`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0375`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.033`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0303`, n `668`, weak_sample_signal
