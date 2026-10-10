# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T00:22:28.829611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `13`; crypto_alt avg `0.3359` n `235`; crypto_major avg `0.2451` n `8`; equity avg `0.0485` n `150`; fx avg `-0.0017` n `6`; index avg `0.0088` n `26`; metal avg `0.0066` n `20`; unknown avg `0.08` n `1116`
- 1h: commodity avg `0.0427` n `13`; crypto_alt avg `0.531` n `235`; crypto_major avg `0.1373` n `8`; equity avg `0.0343` n `150`; fx avg `0.0025` n `6`; index avg `0.0141` n `26`; metal avg `0.0141` n `20`; unknown avg `0.0544` n `1108`
- 4h: commodity avg `-0.0145` n `13`; crypto_alt avg `1.4883` n `235`; crypto_major avg `0.5389` n `8`; equity avg `0.0499` n `150`; fx avg `-0.0032` n `6`; index avg `0.0172` n `26`; metal avg `-0.0122` n `20`; unknown avg `0.2979` n `1092`
- 24h: commodity avg `-0.1605` n `13`; crypto_alt avg `3.2274` n `235`; crypto_major avg `0.8891` n `8`; equity avg `0.8846` n `150`; fx avg `-0.0223` n `6`; index avg `0.1368` n `26`; metal avg `0.4795` n `20`; unknown avg `13.2473` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
