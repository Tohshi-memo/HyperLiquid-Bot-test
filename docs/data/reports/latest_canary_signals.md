# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T06:22:30.109377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `13`; crypto_alt avg `0.0211` n `235`; crypto_major avg `-0.0458` n `8`; equity avg `-0.0247` n `150`; fx avg `0.0121` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.0969` n `1076`
- 1h: commodity avg `0.0596` n `13`; crypto_alt avg `0.1025` n `235`; crypto_major avg `0.1054` n `8`; equity avg `0.009` n `150`; fx avg `0.0037` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0426` n `20`; unknown avg `0.3279` n `1052`
- 4h: commodity avg `0.1509` n `13`; crypto_alt avg `-0.1424` n `235`; crypto_major avg `0.3971` n `8`; equity avg `0.1663` n `150`; fx avg `-0.0374` n `6`; index avg `-0.0012` n `26`; metal avg `-0.1194` n `20`; unknown avg `1.042` n `1046`
- 24h: commodity avg `0.824` n `13`; crypto_alt avg `-2.8133` n `235`; crypto_major avg `-1.748` n `8`; equity avg `-0.2035` n `149`; fx avg `0.0512` n `6`; index avg `-0.0891` n `26`; metal avg `-0.1463` n `20`; unknown avg `870.8641` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
