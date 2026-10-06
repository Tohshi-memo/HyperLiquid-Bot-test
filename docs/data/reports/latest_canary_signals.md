# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T03:22:35.328360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `13`; crypto_alt avg `0.0081` n `235`; crypto_major avg `-0.0599` n `8`; equity avg `0.0584` n `149`; fx avg `-0.011` n `6`; index avg `0.0039` n `26`; metal avg `-0.0101` n `20`; unknown avg `-0.1156` n `1074`
- 1h: commodity avg `0.0232` n `13`; crypto_alt avg `-0.3352` n `235`; crypto_major avg `-0.2253` n `8`; equity avg `-0.0296` n `149`; fx avg `-0.002` n `6`; index avg `-0.01` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.247` n `1072`
- 4h: commodity avg `0.0934` n `13`; crypto_alt avg `-1.3063` n `235`; crypto_major avg `-0.5978` n `8`; equity avg `-0.1791` n `149`; fx avg `0.0067` n `6`; index avg `-0.0736` n `26`; metal avg `-0.0638` n `20`; unknown avg `0.3386` n `1066`
- 24h: commodity avg `0.0058` n `13`; crypto_alt avg `-0.9764` n `235`; crypto_major avg `-0.3374` n `8`; equity avg `0.0195` n `149`; fx avg `0.0433` n `6`; index avg `0.0773` n `26`; metal avg `0.024` n `20`; unknown avg `624.5162` n `801`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
