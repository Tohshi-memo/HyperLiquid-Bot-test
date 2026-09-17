# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T19:52:29.496626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `0.0932` n `234`; crypto_major avg `0.1611` n `8`; equity avg `0.0181` n `140`; fx avg `0.0` n `6`; index avg `0.0107` n `26`; metal avg `0.0134` n `20`; unknown avg `2.0069` n `917`
- 1h: commodity avg `-0.1389` n `12`; crypto_alt avg `0.0237` n `234`; crypto_major avg `0.2493` n `8`; equity avg `0.0472` n `140`; fx avg `0.005` n `6`; index avg `0.0228` n `26`; metal avg `-0.0361` n `20`; unknown avg `27.9642` n `915`
- 4h: commodity avg `-0.0356` n `12`; crypto_alt avg `0.3695` n `234`; crypto_major avg `-0.0769` n `8`; equity avg `0.0866` n `140`; fx avg `0.0279` n `6`; index avg `0.0217` n `26`; metal avg `-0.1781` n `20`; unknown avg `1.8976` n `909`
- 24h: commodity avg `-0.1237` n `12`; crypto_alt avg `4.3362` n `234`; crypto_major avg `1.7832` n `8`; equity avg `2.6686` n `138`; fx avg `0.0156` n `6`; index avg `0.5129` n `26`; metal avg `0.6134` n `20`; unknown avg `3.5561` n `749`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
