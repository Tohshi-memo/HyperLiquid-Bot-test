# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T11:07:25.834448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `0.0051` n `235`; crypto_major avg `-0.0758` n `8`; equity avg `0.0006` n `143`; fx avg `-0.0006` n `6`; index avg `0.0025` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.8625` n `1077`
- 1h: commodity avg `0.014` n `13`; crypto_alt avg `-0.1507` n `235`; crypto_major avg `-0.1144` n `8`; equity avg `0.0038` n `143`; fx avg `0.0191` n `6`; index avg `0.0014` n `26`; metal avg `-0.005` n `20`; unknown avg `0.9443` n `1077`
- 4h: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.288` n `235`; crypto_major avg `0.2609` n `8`; equity avg `0.0143` n `143`; fx avg `0.0237` n `6`; index avg `0.006` n `26`; metal avg `-0.0081` n `20`; unknown avg `0.8497` n `1061`
- 24h: commodity avg `0.1142` n `13`; crypto_alt avg `1.6635` n `235`; crypto_major avg `1.2953` n `8`; equity avg `0.2409` n `143`; fx avg `-0.0065` n `6`; index avg `0.0222` n `26`; metal avg `-0.0039` n `20`; unknown avg `1.0896` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
