# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T07:52:29.483447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.0102` n `235`; crypto_major avg `0.014` n `8`; equity avg `-0.0126` n `143`; fx avg `-0.0051` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0049` n `20`; unknown avg `2.1468` n `984`
- 1h: commodity avg `0.0081` n `13`; crypto_alt avg `-0.4521` n `235`; crypto_major avg `-0.08` n `8`; equity avg `-0.0032` n `143`; fx avg `0.008` n `6`; index avg `0.0012` n `26`; metal avg `-0.0064` n `20`; unknown avg `2.3282` n `982`
- 4h: commodity avg `-0.038` n `13`; crypto_alt avg `-0.6816` n `235`; crypto_major avg `-0.1948` n `8`; equity avg `-0.0519` n `143`; fx avg `-0.005` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0088` n `20`; unknown avg `1.1701` n `954`
- 24h: commodity avg `0.3096` n `13`; crypto_alt avg `-2.0595` n `235`; crypto_major avg `-1.816` n `8`; equity avg `0.2909` n `142`; fx avg `0.0015` n `6`; index avg `0.1817` n `26`; metal avg `-0.3385` n `20`; unknown avg `-0.7719` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
