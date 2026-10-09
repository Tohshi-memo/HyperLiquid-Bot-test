# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T17:52:26.231576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0394` n `13`; crypto_alt avg `0.092` n `235`; crypto_major avg `-0.0053` n `8`; equity avg `0.0907` n `150`; fx avg `0.0029` n `6`; index avg `0.007` n `26`; metal avg `0.0245` n `20`; unknown avg `-0.03` n `1092`
- 1h: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.1322` n `235`; crypto_major avg `-0.1053` n `8`; equity avg `0.0889` n `150`; fx avg `0.0135` n `6`; index avg `-0.0092` n `26`; metal avg `0.0154` n `20`; unknown avg `0.7384` n `1090`
- 4h: commodity avg `0.0025` n `13`; crypto_alt avg `0.6364` n `235`; crypto_major avg `0.0087` n `8`; equity avg `0.4818` n `150`; fx avg `0.0147` n `6`; index avg `0.036` n `26`; metal avg `-0.0775` n `20`; unknown avg `-0.2383` n `1014`
- 24h: commodity avg `-0.0285` n `13`; crypto_alt avg `4.7602` n `235`; crypto_major avg `2.8995` n `8`; equity avg `1.6451` n `150`; fx avg `0.0345` n `6`; index avg `0.2579` n `26`; metal avg `0.6587` n `20`; unknown avg `2.5201` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
