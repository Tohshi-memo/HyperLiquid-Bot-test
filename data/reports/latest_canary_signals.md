# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T19:22:26.883981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `0.0511` n `235`; crypto_major avg `0.0683` n `8`; equity avg `0.0037` n `144`; fx avg `0.0013` n `6`; index avg `0.0021` n `26`; metal avg `-0.0001` n `20`; unknown avg `2.6813` n `1078`
- 1h: commodity avg `0.013` n `13`; crypto_alt avg `0.2965` n `235`; crypto_major avg `0.1687` n `8`; equity avg `-0.0155` n `144`; fx avg `0.0069` n `6`; index avg `0.0014` n `26`; metal avg `0.0043` n `20`; unknown avg `1.5933` n `1076`
- 4h: commodity avg `0.0082` n `13`; crypto_alt avg `0.1667` n `235`; crypto_major avg `0.2271` n `8`; equity avg `-0.0091` n `144`; fx avg `-0.0006` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0017` n `20`; unknown avg `1.6767` n `1068`
- 24h: commodity avg `0.0181` n `13`; crypto_alt avg `1.2937` n `235`; crypto_major avg `1.0256` n `8`; equity avg `0.1845` n `144`; fx avg `0.0299` n `6`; index avg `-0.0194` n `26`; metal avg `0.0078` n `20`; unknown avg `0.4529` n `1021`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
