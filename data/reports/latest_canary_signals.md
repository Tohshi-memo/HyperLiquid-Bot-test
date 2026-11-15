# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T14:07:26.196524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `13`; crypto_alt avg `-0.7432` n `239`; crypto_major avg `-0.6868` n `8`; equity avg `-0.1435` n `162`; fx avg `-0.0037` n `6`; index avg `-0.0097` n `27`; metal avg `-0.0088` n `20`; unknown avg `0.2543` n `1258`
- 1h: commodity avg `-0.1128` n `13`; crypto_alt avg `-0.8064` n `239`; crypto_major avg `-0.6142` n `8`; equity avg `-0.1439` n `162`; fx avg `-0.0044` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0111` n `20`; unknown avg `0.1085` n `1262`
- 4h: commodity avg `-0.0903` n `13`; crypto_alt avg `-0.3377` n `239`; crypto_major avg `-0.3085` n `8`; equity avg `-0.0917` n `162`; fx avg `-0.0293` n `6`; index avg `-0.0045` n `27`; metal avg `-0.002` n `20`; unknown avg `0.2899` n `1253`
- 24h: commodity avg `-0.0692` n `13`; crypto_alt avg `-3.1928` n `239`; crypto_major avg `-2.2807` n `8`; equity avg `-0.5425` n `162`; fx avg `-0.0069` n `6`; index avg `-0.0482` n `27`; metal avg `-0.3106` n `20`; unknown avg `0.0612` n `1134`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
