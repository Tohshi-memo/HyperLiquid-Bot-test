# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T13:07:25.031221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0309` n `13`; crypto_alt avg `-0.004` n `239`; crypto_major avg `-0.1785` n `8`; equity avg `-0.0352` n `162`; fx avg `-0.0004` n `6`; index avg `-0.0149` n `27`; metal avg `0.0795` n `20`; unknown avg `6.4924` n `1257`
- 1h: commodity avg `-0.0136` n `13`; crypto_alt avg `-0.2059` n `239`; crypto_major avg `-0.1235` n `8`; equity avg `-0.41` n `162`; fx avg `-0.0117` n `6`; index avg `-0.0202` n `27`; metal avg `0.0276` n `20`; unknown avg `6.7043` n `1249`
- 4h: commodity avg `-0.2618` n `13`; crypto_alt avg `-0.6155` n `239`; crypto_major avg `-0.8614` n `8`; equity avg `-0.6042` n `162`; fx avg `-0.0349` n `6`; index avg `-0.0139` n `27`; metal avg `0.0065` n `20`; unknown avg `25.5727` n `1249`
- 24h: commodity avg `-0.2395` n `13`; crypto_alt avg `-2.7058` n `239`; crypto_major avg `-1.9175` n `8`; equity avg `-1.8623` n `162`; fx avg `-0.0965` n `6`; index avg `-0.1132` n `27`; metal avg `-0.839` n `20`; unknown avg `5.3151` n `1140`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
