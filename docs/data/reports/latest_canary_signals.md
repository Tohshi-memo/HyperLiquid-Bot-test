# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T14:37:29.200224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `13`; crypto_alt avg `-0.3004` n `239`; crypto_major avg `-0.4733` n `8`; equity avg `-0.117` n `162`; fx avg `-0.0014` n `6`; index avg `-0.0109` n `27`; metal avg `-0.0325` n `20`; unknown avg `158.1314` n `1264`
- 1h: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.9643` n `239`; crypto_major avg `-1.0024` n `8`; equity avg `-0.2609` n `162`; fx avg `-0.0023` n `6`; index avg `-0.0101` n `27`; metal avg `-0.0309` n `20`; unknown avg `41.3609` n `1262`
- 4h: commodity avg `-0.0907` n `13`; crypto_alt avg `-0.7398` n `239`; crypto_major avg `-0.6203` n `8`; equity avg `-0.174` n `162`; fx avg `-0.0323` n `6`; index avg `-0.0089` n `27`; metal avg `-0.0173` n `20`; unknown avg `0.1489` n `1249`
- 24h: commodity avg `-0.0149` n `13`; crypto_alt avg `-2.3825` n `239`; crypto_major avg `-1.6248` n `8`; equity avg `-0.3938` n `162`; fx avg `-0.0118` n `6`; index avg `-0.0294` n `27`; metal avg `-0.298` n `20`; unknown avg `0.1025` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
