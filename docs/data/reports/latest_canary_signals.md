# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T05:37:42.019130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.2185` n `235`; crypto_major avg `0.0609` n `8`; equity avg `-0.0055` n `143`; fx avg `-0.0187` n `6`; index avg `-0.0045` n `26`; metal avg `0.0003` n `20`; unknown avg `0.7834` n `1079`
- 1h: commodity avg `0.0328` n `13`; crypto_alt avg `0.2726` n `235`; crypto_major avg `0.1082` n `8`; equity avg `0.0292` n `143`; fx avg `-0.0183` n `6`; index avg `0.0047` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.9078` n `1077`
- 4h: commodity avg `-0.037` n `13`; crypto_alt avg `0.7617` n `235`; crypto_major avg `0.2713` n `8`; equity avg `0.0713` n `143`; fx avg `-0.0182` n `6`; index avg `0.0031` n `26`; metal avg `0.008` n `20`; unknown avg `0.9329` n `1071`
- 24h: commodity avg `0.2142` n `13`; crypto_alt avg `1.8399` n `235`; crypto_major avg `0.7538` n `8`; equity avg `0.2655` n `143`; fx avg `-0.0374` n `6`; index avg `0.0076` n `26`; metal avg `0.0012` n `20`; unknown avg `0.2625` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
