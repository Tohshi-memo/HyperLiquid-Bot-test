# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T08:07:24.808216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `13`; crypto_alt avg `0.1747` n `239`; crypto_major avg `0.2289` n `8`; equity avg `0.2906` n `161`; fx avg `0.0` n `6`; index avg `0.0186` n `27`; metal avg `-0.0143` n `20`; unknown avg `0.2537` n `1241`
- 1h: commodity avg `0.059` n `13`; crypto_alt avg `0.5839` n `239`; crypto_major avg `0.6606` n `8`; equity avg `0.3476` n `161`; fx avg `0.0115` n `6`; index avg `0.0141` n `27`; metal avg `-0.0559` n `20`; unknown avg `0.4658` n `1237`
- 4h: commodity avg `0.0142` n `13`; crypto_alt avg `-0.7703` n `239`; crypto_major avg `-0.0596` n `8`; equity avg `0.5109` n `161`; fx avg `-0.0433` n `6`; index avg `0.0115` n `27`; metal avg `0.1138` n `20`; unknown avg `0.1183` n `1201`
- 24h: commodity avg `0.4441` n `13`; crypto_alt avg `-1.0543` n `239`; crypto_major avg `-2.0177` n `8`; equity avg `1.7293` n `161`; fx avg `-0.1784` n `6`; index avg `0.1925` n `27`; metal avg `-0.0139` n `20`; unknown avg `1.7748` n `1158`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
