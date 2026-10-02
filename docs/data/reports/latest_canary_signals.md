# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T22:37:28.859661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `13`; crypto_alt avg `0.3883` n `235`; crypto_major avg `0.2688` n `8`; equity avg `0.0125` n `143`; fx avg `-0.0008` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0065` n `20`; unknown avg `0.9833` n `984`
- 1h: commodity avg `0.0496` n `13`; crypto_alt avg `0.5675` n `235`; crypto_major avg `0.4135` n `8`; equity avg `0.0385` n `143`; fx avg `-0.0092` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.5235` n `966`
- 4h: commodity avg `0.3521` n `13`; crypto_alt avg `-0.118` n `235`; crypto_major avg `-0.0713` n `8`; equity avg `0.1872` n `143`; fx avg `-0.0216` n `6`; index avg `0.0318` n `26`; metal avg `0.0623` n `20`; unknown avg `-0.0252` n `906`
- 24h: commodity avg `0.1309` n `13`; crypto_alt avg `-0.8142` n `235`; crypto_major avg `-0.5614` n `8`; equity avg `0.7453` n `142`; fx avg `-0.1659` n `6`; index avg `0.287` n `26`; metal avg `-0.2296` n `20`; unknown avg `-0.3835` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
