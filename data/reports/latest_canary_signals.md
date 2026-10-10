# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T02:26:48.128003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `13`; crypto_alt avg `-0.0277` n `235`; crypto_major avg `-0.0731` n `8`; equity avg `-0.0153` n `150`; fx avg `-0.0019` n `6`; index avg `-0.007` n `26`; metal avg `0.0012` n `20`; unknown avg `0.0571` n `1116`
- 1h: commodity avg `-0.0549` n `13`; crypto_alt avg `0.4437` n `235`; crypto_major avg `0.1631` n `8`; equity avg `-0.0088` n `150`; fx avg `-0.0041` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0103` n `20`; unknown avg `-0.0925` n `1114`
- 4h: commodity avg `0.0638` n `13`; crypto_alt avg `1.4787` n `235`; crypto_major avg `0.4755` n `8`; equity avg `0.0661` n `150`; fx avg `0.0032` n `6`; index avg `0.0376` n `26`; metal avg `0.0197` n `20`; unknown avg `0.1925` n `1108`
- 24h: commodity avg `-0.0917` n `13`; crypto_alt avg `2.6967` n `235`; crypto_major avg `0.624` n `8`; equity avg `0.4947` n `150`; fx avg `-0.0249` n `6`; index avg `0.0825` n `26`; metal avg `0.1858` n `20`; unknown avg `13.1003` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
