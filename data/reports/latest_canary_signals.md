# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T11:07:26.839689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0794` n `13`; crypto_alt avg `-0.0543` n `239`; crypto_major avg `-0.1562` n `8`; equity avg `-0.0034` n `158`; fx avg `-0.0146` n `6`; index avg `0.0081` n `27`; metal avg `0.013` n `20`; unknown avg `0.456` n `1259`
- 1h: commodity avg `-0.2878` n `13`; crypto_alt avg `-0.0577` n `239`; crypto_major avg `-0.203` n `8`; equity avg `-0.0766` n `158`; fx avg `-0.0109` n `6`; index avg `0.0079` n `27`; metal avg `-0.006` n `20`; unknown avg `0.5456` n `1257`
- 4h: commodity avg `-0.1329` n `13`; crypto_alt avg `0.9799` n `239`; crypto_major avg `-0.0836` n `8`; equity avg `0.5595` n `158`; fx avg `0.0741` n `6`; index avg `0.0734` n `27`; metal avg `0.0017` n `20`; unknown avg `170.6423` n `1129`
- 24h: commodity avg `-0.2391` n `13`; crypto_alt avg `-1.8052` n `239`; crypto_major avg `-3.7276` n `8`; equity avg `-0.4158` n `158`; fx avg `-0.1077` n `6`; index avg `-0.0255` n `27`; metal avg `0.2727` n `20`; unknown avg `-0.0182` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
