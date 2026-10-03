# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T19:22:29.987826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `13`; crypto_alt avg `0.019` n `235`; crypto_major avg `0.0194` n `8`; equity avg `0.0155` n `143`; fx avg `0.0005` n `6`; index avg `0.0035` n `26`; metal avg `0.002` n `20`; unknown avg `0.5104` n `1070`
- 1h: commodity avg `-0.0012` n `13`; crypto_alt avg `0.0023` n `235`; crypto_major avg `-0.0209` n `8`; equity avg `0.0167` n `143`; fx avg `-0.0033` n `6`; index avg `0.0053` n `26`; metal avg `0.001` n `20`; unknown avg `1.5394` n `1068`
- 4h: commodity avg `-0.029` n `13`; crypto_alt avg `0.1733` n `235`; crypto_major avg `0.2334` n `8`; equity avg `0.0913` n `143`; fx avg `-0.016` n `6`; index avg `0.027` n `26`; metal avg `0.004` n `20`; unknown avg `2.0605` n `1062`
- 24h: commodity avg `0.2104` n `13`; crypto_alt avg `2.9179` n `235`; crypto_major avg `1.7299` n `8`; equity avg `0.2322` n `143`; fx avg `-0.0554` n `6`; index avg `0.0663` n `26`; metal avg `-0.0218` n `20`; unknown avg `1.7076` n `860`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
