# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T11:22:30.002696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `13`; crypto_alt avg `0.1379` n `235`; crypto_major avg `0.1611` n `8`; equity avg `0.1688` n `150`; fx avg `0.0313` n `6`; index avg `0.0442` n `26`; metal avg `0.1076` n `20`; unknown avg `0.2073` n `1074`
- 1h: commodity avg `-0.0388` n `13`; crypto_alt avg `0.19` n `235`; crypto_major avg `0.1988` n `8`; equity avg `0.1743` n `150`; fx avg `0.0386` n `6`; index avg `0.0617` n `26`; metal avg `0.0974` n `20`; unknown avg `-0.2387` n `1072`
- 4h: commodity avg `-0.2993` n `13`; crypto_alt avg `0.8714` n `235`; crypto_major avg `0.7469` n `8`; equity avg `0.4252` n `149`; fx avg `0.0584` n `6`; index avg `0.1008` n `26`; metal avg `0.1219` n `20`; unknown avg `0.8623` n `1056`
- 24h: commodity avg `-0.658` n `13`; crypto_alt avg `-0.3392` n `235`; crypto_major avg `-0.1213` n `8`; equity avg `0.7756` n `149`; fx avg `0.0619` n `6`; index avg `0.2593` n `26`; metal avg `-0.0975` n `20`; unknown avg `-0.0205` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
