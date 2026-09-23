# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T04:37:35.025162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `0.1628` n `234`; crypto_major avg `0.1009` n `8`; equity avg `0.0889` n `140`; fx avg `-0.0217` n `6`; index avg `0.0058` n `26`; metal avg `0.014` n `20`; unknown avg `-0.1336` n `945`
- 1h: commodity avg `-0.0154` n `12`; crypto_alt avg `0.1124` n `234`; crypto_major avg `0.576` n `8`; equity avg `0.3794` n `140`; fx avg `-0.0412` n `6`; index avg `0.0323` n `26`; metal avg `0.0728` n `20`; unknown avg `0.218` n `937`
- 4h: commodity avg `-0.1555` n `12`; crypto_alt avg `0.8665` n `234`; crypto_major avg `1.2565` n `8`; equity avg `-0.0822` n `140`; fx avg `-0.0257` n `6`; index avg `-0.0279` n `26`; metal avg `-0.1803` n `20`; unknown avg `-0.2146` n `937`
- 24h: commodity avg `-0.145` n `12`; crypto_alt avg `4.1926` n `234`; crypto_major avg `2.9475` n `8`; equity avg `1.0582` n `140`; fx avg `-0.2058` n `6`; index avg `0.0853` n `26`; metal avg `0.1686` n `20`; unknown avg `1.8547` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
