# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T06:37:28.407945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `0.0374` n `235`; crypto_major avg `0.0477` n `8`; equity avg `0.0159` n `143`; fx avg `-0.0111` n `6`; index avg `0.0` n `26`; metal avg `-0.005` n `20`; unknown avg `-0.0407` n `984`
- 1h: commodity avg `0.0108` n `13`; crypto_alt avg `-0.1509` n `235`; crypto_major avg `-0.0884` n `8`; equity avg `-0.0202` n `143`; fx avg `-0.0045` n `6`; index avg `-0.013` n `26`; metal avg `-0.0032` n `20`; unknown avg `2.5452` n `960`
- 4h: commodity avg `-0.0824` n `13`; crypto_alt avg `0.0489` n `235`; crypto_major avg `-0.128` n `8`; equity avg `-0.1083` n `143`; fx avg `-0.015` n `6`; index avg `-0.0174` n `26`; metal avg `-0.0105` n `20`; unknown avg `-0.2178` n `954`
- 24h: commodity avg `0.1304` n `13`; crypto_alt avg `-1.456` n `235`; crypto_major avg `-1.834` n `8`; equity avg `0.4725` n `142`; fx avg `-0.0344` n `6`; index avg `0.2297` n `26`; metal avg `-0.3238` n `20`; unknown avg `-0.9027` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
