# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T12:07:31.399326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `-0.0653` n `239`; crypto_major avg `-0.0364` n `8`; equity avg `0.1276` n `162`; fx avg `0.0042` n `6`; index avg `-0.0203` n `27`; metal avg `-0.0058` n `20`; unknown avg `0.1234` n `1254`
- 1h: commodity avg `0.0492` n `13`; crypto_alt avg `0.6879` n `239`; crypto_major avg `0.5946` n `8`; equity avg `1.0922` n `162`; fx avg `0.0216` n `6`; index avg `0.0682` n `27`; metal avg `0.093` n `20`; unknown avg `0.5861` n `1252`
- 4h: commodity avg `0.2141` n `13`; crypto_alt avg `0.3647` n `239`; crypto_major avg `0.134` n `8`; equity avg `0.6975` n `162`; fx avg `-0.0179` n `6`; index avg `0.0472` n `27`; metal avg `0.1035` n `20`; unknown avg `19.29` n `1254`
- 24h: commodity avg `-0.6375` n `13`; crypto_alt avg `1.4696` n `239`; crypto_major avg `1.6386` n `8`; equity avg `-1.0424` n `162`; fx avg `-0.033` n `6`; index avg `-0.1294` n `27`; metal avg `-0.1119` n `20`; unknown avg `13.0062` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
