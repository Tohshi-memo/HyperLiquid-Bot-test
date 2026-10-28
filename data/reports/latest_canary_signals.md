# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T07:52:40.182857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0462` n `13`; crypto_alt avg `0.156` n `238`; crypto_major avg `0.1588` n `8`; equity avg `-0.0749` n `154`; fx avg `0.0145` n `6`; index avg `-0.0224` n `27`; metal avg `-0.0053` n `20`; unknown avg `0.4791` n `1238`
- 1h: commodity avg `0.0671` n `13`; crypto_alt avg `0.114` n `238`; crypto_major avg `0.1449` n `8`; equity avg `-0.0674` n `154`; fx avg `0.0005` n `6`; index avg `-0.008` n `27`; metal avg `0.0258` n `20`; unknown avg `0.4992` n `1228`
- 4h: commodity avg `0.1509` n `13`; crypto_alt avg `-0.4112` n `238`; crypto_major avg `-0.2236` n `8`; equity avg `-0.0725` n `154`; fx avg `-0.0571` n `6`; index avg `-0.0214` n `27`; metal avg `-0.0842` n `20`; unknown avg `2.3109` n `1202`
- 24h: commodity avg `-0.1343` n `13`; crypto_alt avg `1.487` n `238`; crypto_major avg `1.861` n `8`; equity avg `3.9949` n `154`; fx avg `0.0484` n `6`; index avg `0.5352` n `27`; metal avg `0.3692` n `20`; unknown avg `17.0378` n `1014`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
