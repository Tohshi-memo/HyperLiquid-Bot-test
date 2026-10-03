# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T05:52:31.433325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0168` n `13`; crypto_alt avg `-0.0155` n `235`; crypto_major avg `-0.0779` n `8`; equity avg `-0.0036` n `143`; fx avg `-0.0079` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.4489` n `984`
- 1h: commodity avg `-0.0531` n `13`; crypto_alt avg `0.1402` n `235`; crypto_major avg `0.1075` n `8`; equity avg `-0.0006` n `143`; fx avg `-0.0194` n `6`; index avg `0.0129` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.2526` n `982`
- 4h: commodity avg `-0.0951` n `13`; crypto_alt avg `0.358` n `235`; crypto_major avg `-0.1715` n `8`; equity avg `-0.0601` n `143`; fx avg `-0.0213` n `6`; index avg `0.0051` n `26`; metal avg `0.0077` n `20`; unknown avg `-0.4331` n `976`
- 24h: commodity avg `-0.003` n `13`; crypto_alt avg `-1.2213` n `235`; crypto_major avg `-1.6791` n `8`; equity avg `0.5262` n `142`; fx avg `-0.0803` n `6`; index avg `0.2662` n `26`; metal avg `-0.3301` n `20`; unknown avg `-0.826` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
