# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T08:22:24.845616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1003` n `13`; crypto_alt avg `-0.0405` n `235`; crypto_major avg `-0.0331` n `8`; equity avg `0.1002` n `150`; fx avg `-0.0119` n `6`; index avg `0.0113` n `26`; metal avg `0.0351` n `20`; unknown avg `0.1644` n `1066`
- 1h: commodity avg `-0.1825` n `13`; crypto_alt avg `-0.0925` n `235`; crypto_major avg `0.0189` n `8`; equity avg `0.092` n `150`; fx avg `0.0229` n `6`; index avg `0.0256` n `26`; metal avg `0.0509` n `20`; unknown avg `-0.0911` n `1006`
- 4h: commodity avg `-0.0857` n `13`; crypto_alt avg `0.4108` n `235`; crypto_major avg `0.2295` n `8`; equity avg `0.6352` n `150`; fx avg `0.0483` n `6`; index avg `0.0887` n `26`; metal avg `0.1878` n `20`; unknown avg `2.18` n `988`
- 24h: commodity avg `-0.4495` n `13`; crypto_alt avg `-1.1398` n `235`; crypto_major avg `-1.8265` n `8`; equity avg `-0.4283` n `150`; fx avg `0.1463` n `6`; index avg `0.0491` n `26`; metal avg `0.506` n `20`; unknown avg `7.2796` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
