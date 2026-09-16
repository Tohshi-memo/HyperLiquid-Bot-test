# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T11:38:03.105792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `12`; crypto_alt avg `0.1841` n `234`; crypto_major avg `0.2744` n `8`; equity avg `0.1343` n `137`; fx avg `-0.0384` n `6`; index avg `0.026` n `27`; metal avg `0.0133` n `20`; unknown avg `9.4918` n `919`
- 1h: commodity avg `-0.1105` n `12`; crypto_alt avg `0.2785` n `234`; crypto_major avg `0.4506` n `8`; equity avg `0.1893` n `137`; fx avg `-0.0517` n `6`; index avg `0.0179` n `27`; metal avg `0.0425` n `20`; unknown avg `0.5124` n `917`
- 4h: commodity avg `-0.035` n `12`; crypto_alt avg `0.3641` n `234`; crypto_major avg `0.5484` n `8`; equity avg `0.1856` n `137`; fx avg `-0.0277` n `6`; index avg `0.0327` n `27`; metal avg `0.0067` n `20`; unknown avg `-0.1605` n `911`
- 24h: commodity avg `0.227` n `12`; crypto_alt avg `-2.1251` n `234`; crypto_major avg `-2.0719` n `8`; equity avg `-0.1053` n `137`; fx avg `0.0736` n `6`; index avg `0.0606` n `27`; metal avg `0.5008` n `20`; unknown avg `18891.4929` n `798`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
