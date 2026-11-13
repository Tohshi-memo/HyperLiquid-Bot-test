# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T07:07:26.674488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0489` n `13`; crypto_alt avg `0.591` n `239`; crypto_major avg `0.5067` n `8`; equity avg `0.3249` n `162`; fx avg `0.0213` n `6`; index avg `0.0357` n `27`; metal avg `0.0686` n `20`; unknown avg `4.0134` n `1256`
- 1h: commodity avg `-0.0061` n `13`; crypto_alt avg `1.7293` n `239`; crypto_major avg `1.38` n `8`; equity avg `0.4968` n `162`; fx avg `0.0107` n `6`; index avg `0.0401` n `27`; metal avg `0.0571` n `20`; unknown avg `204.3141` n `1252`
- 4h: commodity avg `0.0195` n `13`; crypto_alt avg `0.396` n `239`; crypto_major avg `-0.6565` n `8`; equity avg `-0.8456` n `162`; fx avg `0.0534` n `6`; index avg `-0.1236` n `27`; metal avg `-0.1639` n `20`; unknown avg `3.1201` n `1218`
- 24h: commodity avg `0.6204` n `13`; crypto_alt avg `-0.8075` n `239`; crypto_major avg `-2.8871` n `8`; equity avg `-1.0115` n `162`; fx avg `-0.0002` n `6`; index avg `0.0429` n `27`; metal avg `-0.4508` n `20`; unknown avg `98.474` n `1133`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
