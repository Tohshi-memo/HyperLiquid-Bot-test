# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T07:22:29.489909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `12`; crypto_alt avg `0.145` n `228`; crypto_major avg `0.0124` n `8`; equity avg `-0.1089` n `74`; fx avg `0.0203` n `6`; index avg `-0.0081` n `23`; metal avg `-0.0804` n `18`; unknown avg `0.1261` n `547`
- 1h: commodity avg `0.265` n `12`; crypto_alt avg `-0.095` n `228`; crypto_major avg `-0.1541` n `8`; equity avg `-0.1686` n `74`; fx avg `0.0602` n `6`; index avg `-0.0632` n `23`; metal avg `-0.2363` n `18`; unknown avg `0.1487` n `547`
- 4h: commodity avg `0.028` n `12`; crypto_alt avg `1.6958` n `228`; crypto_major avg `0.9702` n `8`; equity avg `0.8765` n `74`; fx avg `0.0243` n `6`; index avg `0.4268` n `23`; metal avg `0.3482` n `18`; unknown avg `0.4255` n `503`
- 24h: commodity avg `-1.2768` n `12`; crypto_alt avg `0.6705` n `228`; crypto_major avg `0.8912` n `8`; equity avg `2.6514` n `74`; fx avg `-0.0714` n `6`; index avg `1.1772` n `23`; metal avg `0.5058` n `18`; unknown avg `-2.7119` n `503`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
