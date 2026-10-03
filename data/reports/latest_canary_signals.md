# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T01:52:30.376504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `13`; crypto_alt avg `-0.1316` n `235`; crypto_major avg `-0.0655` n `8`; equity avg `0.021` n `143`; fx avg `0.0047` n `6`; index avg `0.0042` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.0932` n `984`
- 1h: commodity avg `-0.1129` n `13`; crypto_alt avg `-0.3065` n `235`; crypto_major avg `-0.0771` n `8`; equity avg `0.0156` n `143`; fx avg `0.0149` n `6`; index avg `0.0157` n `26`; metal avg `-0.0155` n `20`; unknown avg `-0.0853` n `982`
- 4h: commodity avg `-0.1616` n `13`; crypto_alt avg `1.2594` n `235`; crypto_major avg `0.944` n `8`; equity avg `0.0873` n `143`; fx avg `0.0162` n `6`; index avg `0.0091` n `26`; metal avg `-0.0116` n `20`; unknown avg `1.2158` n `968`
- 24h: commodity avg `0.0371` n `13`; crypto_alt avg `-0.4511` n `235`; crypto_major avg `-0.1909` n `8`; equity avg `0.7822` n `142`; fx avg `-0.1312` n `6`; index avg `0.2878` n `26`; metal avg `-0.0108` n `20`; unknown avg `-0.4554` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
