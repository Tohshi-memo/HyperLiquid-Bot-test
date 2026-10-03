# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T03:52:35.208505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `0.1515` n `235`; crypto_major avg `0.0907` n `8`; equity avg `-0.0031` n `143`; fx avg `0.0001` n `6`; index avg `0.0005` n `26`; metal avg `0.0058` n `20`; unknown avg `-0.0706` n `984`
- 1h: commodity avg `0.0036` n `13`; crypto_alt avg `0.3855` n `235`; crypto_major avg `0.0434` n `8`; equity avg `-0.031` n `143`; fx avg `-0.0124` n `6`; index avg `-0.0021` n `26`; metal avg `0.006` n `20`; unknown avg `-0.2002` n `982`
- 4h: commodity avg `-0.1765` n `13`; crypto_alt avg `0.5391` n `235`; crypto_major avg `0.098` n `8`; equity avg `-0.015` n `143`; fx avg `0.0153` n `6`; index avg `0.0318` n `26`; metal avg `-0.0049` n `20`; unknown avg `-0.2661` n `976`
- 24h: commodity avg `0.0401` n `13`; crypto_alt avg `-0.1749` n `235`; crypto_major avg `-0.831` n `8`; equity avg `0.6287` n `142`; fx avg `-0.1246` n `6`; index avg `0.2717` n `26`; metal avg `-0.2261` n `20`; unknown avg `-0.8222` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
