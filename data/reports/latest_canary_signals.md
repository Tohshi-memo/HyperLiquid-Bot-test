# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T14:07:40.580132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0759` n `13`; crypto_alt avg `0.1198` n `239`; crypto_major avg `0.1163` n `8`; equity avg `0.4987` n `165`; fx avg `-0.0159` n `6`; index avg `0.0522` n `27`; metal avg `-0.0215` n `20`; unknown avg `0.3586` n `1252`
- 1h: commodity avg `0.161` n `13`; crypto_alt avg `0.205` n `239`; crypto_major avg `0.298` n `8`; equity avg `0.6863` n `165`; fx avg `-0.0215` n `6`; index avg `0.0833` n `27`; metal avg `-0.0187` n `20`; unknown avg `159.3678` n `1258`
- 4h: commodity avg `0.4844` n `13`; crypto_alt avg `-1.0168` n `239`; crypto_major avg `-0.889` n `8`; equity avg `0.0748` n `165`; fx avg `0.0407` n `6`; index avg `0.0039` n `27`; metal avg `0.0013` n `20`; unknown avg `479.0075` n `1252`
- 24h: commodity avg `-0.399` n `13`; crypto_alt avg `-4.4223` n `239`; crypto_major avg `-4.0472` n `8`; equity avg `-7.6331` n `165`; fx avg `-0.0614` n `6`; index avg `-0.748` n `27`; metal avg `-1.2446` n `20`; unknown avg `21.2059` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
