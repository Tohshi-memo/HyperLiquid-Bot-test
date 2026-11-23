# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T21:37:28.421412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3759` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `0.2487` n `239`; crypto_major avg `0.1678` n `8`; equity avg `0.134` n `166`; fx avg `-0.0007` n `6`; index avg `0.0184` n `27`; metal avg `-0.0117` n `20`; unknown avg `157.7372` n `1266`
- 1h: commodity avg `0.0322` n `13`; crypto_alt avg `-0.0986` n `239`; crypto_major avg `0.0519` n `8`; equity avg `-0.0833` n `166`; fx avg `-0.012` n `6`; index avg `-0.0131` n `27`; metal avg `-0.0559` n `20`; unknown avg `-0.3567` n `1234`
- 4h: commodity avg `-0.1291` n `13`; crypto_alt avg `-1.6086` n `239`; crypto_major avg `-1.4056` n `8`; equity avg `-0.3421` n `166`; fx avg `-0.0146` n `6`; index avg `-0.0297` n `27`; metal avg `-0.2247` n `20`; unknown avg `328.059` n `1226`
- 24h: commodity avg `-1.4381` n `13`; crypto_alt avg `1.0395` n `239`; crypto_major avg `1.3486` n `8`; equity avg `5.9143` n `166`; fx avg `-0.1384` n `6`; index avg `0.5791` n `27`; metal avg `0.5744` n `20`; unknown avg `118.4693` n `1050`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
