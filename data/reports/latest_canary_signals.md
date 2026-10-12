# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T21:22:30.464469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0375` n `13`; crypto_alt avg `0.0429` n `235`; crypto_major avg `0.0905` n `8`; equity avg `-0.0198` n `151`; fx avg `-0.0027` n `6`; index avg `0.0239` n `26`; metal avg `0.0065` n `20`; unknown avg `0.1052` n `1135`
- 1h: commodity avg `0.048` n `13`; crypto_alt avg `-0.2023` n `235`; crypto_major avg `-0.2236` n `8`; equity avg `-0.0188` n `151`; fx avg `-0.0063` n `6`; index avg `0.006` n `26`; metal avg `0.0443` n `20`; unknown avg `0.7786` n `1104`
- 4h: commodity avg `-0.1454` n `13`; crypto_alt avg `0.1461` n `235`; crypto_major avg `0.1366` n `8`; equity avg `-0.004` n `151`; fx avg `-0.0247` n `6`; index avg `-0.0078` n `26`; metal avg `0.0541` n `20`; unknown avg `0.8505` n `1078`
- 24h: commodity avg `0.2155` n `13`; crypto_alt avg `-2.2089` n `235`; crypto_major avg `-1.1993` n `8`; equity avg `-3.3378` n `151`; fx avg `-0.1706` n `6`; index avg `-0.3239` n `26`; metal avg `-0.1049` n `20`; unknown avg `3.589` n `885`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2068`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1774`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0939`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0885`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `666`, weak_sample_signal
