# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T15:37:29.610814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `13`; crypto_alt avg `-0.0514` n `235`; crypto_major avg `0.0025` n `8`; equity avg `0.07` n `151`; fx avg `-0.011` n `6`; index avg `0.0204` n `26`; metal avg `0.0097` n `20`; unknown avg `0.3624` n `1134`
- 1h: crypto_alt avg `-0.3273` n `227`; crypto_major avg `-0.1985` n `7`; metal avg `-0.0192` n `1`; unknown avg `0.0629` n `1039`
- 4h: commodity avg `0.4256` n `13`; crypto_alt avg `-1.5211` n `235`; crypto_major avg `-1.0919` n `8`; equity avg `-1.6352` n `151`; fx avg `-0.0276` n `6`; index avg `-0.0992` n `26`; metal avg `-0.1411` n `20`; unknown avg `-0.0086` n `1074`
- 24h: commodity avg `0.5976` n `13`; crypto_alt avg `-1.6776` n `235`; crypto_major avg `-0.8158` n `8`; equity avg `-3.0411` n `151`; fx avg `-0.1408` n `6`; index avg `-0.2703` n `26`; metal avg `-0.1205` n `20`; unknown avg `-0.3502` n `881`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2315`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2191`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1209`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1117`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1058`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0985`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.092`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0871`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0726`, n `666`, weak_sample_signal
