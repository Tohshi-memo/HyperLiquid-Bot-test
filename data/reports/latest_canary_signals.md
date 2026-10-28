# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T16:55:03.774455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.55` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1714` n `13`; crypto_alt avg `0.1586` n `238`; crypto_major avg `0.2233` n `8`; equity avg `0.2252` n `155`; fx avg `-0.001` n `6`; index avg `0.0613` n `27`; metal avg `0.0606` n `20`; unknown avg `2.2675` n `1234`
- 1h: commodity avg `-0.1583` n `13`; crypto_alt avg `-0.0` n `238`; crypto_major avg `0.2612` n `8`; equity avg `0.1943` n `155`; fx avg `0.0366` n `6`; index avg `0.0559` n `27`; metal avg `0.065` n `20`; unknown avg `1.7234` n `1224`
- 4h: commodity avg `0.071` n `13`; crypto_alt avg `0.0313` n `238`; crypto_major avg `-0.1678` n `8`; equity avg `0.0402` n `155`; fx avg `0.1186` n `6`; index avg `0.1009` n `27`; metal avg `-0.1087` n `20`; unknown avg `3.5383` n `1150`
- 24h: commodity avg `0.5531` n `13`; crypto_alt avg `0.1597` n `238`; crypto_major avg `0.1595` n `8`; equity avg `1.3333` n `154`; fx avg `0.2575` n `6`; index avg `0.3019` n `27`; metal avg `-0.0935` n `20`; unknown avg `2.3964` n `1100`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
