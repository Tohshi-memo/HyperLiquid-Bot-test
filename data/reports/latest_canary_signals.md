# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T10:07:33.057030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `13`; crypto_alt avg `0.0547` n `235`; crypto_major avg `0.0707` n `8`; equity avg `0.014` n `143`; fx avg `0.0` n `6`; index avg `0.0024` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.0241` n `1077`
- 1h: commodity avg `-0.0203` n `13`; crypto_alt avg `-0.035` n `235`; crypto_major avg `0.2874` n `8`; equity avg `0.0243` n `143`; fx avg `0.0025` n `6`; index avg `0.0096` n `26`; metal avg `-0.0085` n `20`; unknown avg `0.5853` n `1077`
- 4h: commodity avg `-0.0328` n `13`; crypto_alt avg `-0.0014` n `235`; crypto_major avg `0.5275` n `8`; equity avg `0.0033` n `143`; fx avg `0.0067` n `6`; index avg `0.0034` n `26`; metal avg `-0.0075` n `20`; unknown avg `0.2197` n `1061`
- 24h: commodity avg `0.0932` n `13`; crypto_alt avg `1.9587` n `235`; crypto_major avg `1.4761` n `8`; equity avg `0.2519` n `143`; fx avg `-0.0271` n `6`; index avg `0.028` n `26`; metal avg `0.0029` n `20`; unknown avg `0.0466` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
