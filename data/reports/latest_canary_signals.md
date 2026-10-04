# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T04:52:31.999058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `13`; crypto_alt avg `0.0641` n `235`; crypto_major avg `0.0157` n `8`; equity avg `0.0227` n `143`; fx avg `0.0012` n `6`; index avg `0.0024` n `26`; metal avg `0.0006` n `20`; unknown avg `0.2146` n `1079`
- 1h: commodity avg `0.0018` n `13`; crypto_alt avg `0.3721` n `235`; crypto_major avg `0.0009` n `8`; equity avg `0.0159` n `143`; fx avg `-0.0031` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.1711` n `1071`
- 4h: commodity avg `-0.0047` n `13`; crypto_alt avg `0.43` n `235`; crypto_major avg `0.1412` n `8`; equity avg `0.0567` n `143`; fx avg `-0.001` n `6`; index avg `-0.0064` n `26`; metal avg `0.0126` n `20`; unknown avg `0.1534` n `1071`
- 24h: commodity avg `0.1268` n `13`; crypto_alt avg `1.7798` n `235`; crypto_major avg `0.8483` n `8`; equity avg `0.2619` n `143`; fx avg `-0.0295` n `6`; index avg `0.02` n `26`; metal avg `0.0081` n `20`; unknown avg `0.2592` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
