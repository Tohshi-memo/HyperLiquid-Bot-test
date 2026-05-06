# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T17:22:21.319438+00:00`
- Correlation status: `ready`
- Asset price records: `473`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `6.06` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.267` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0909` n `12`; crypto_alt avg `-0.2549` n `228`; crypto_major avg `-0.1564` n `8`; equity avg `0.0058` n `65`; fx avg `-0.0086` n `4`; index avg `0.0174` n `23`; metal avg `-0.0978` n `18`; unknown avg `-0.0935` n `356`
- 1h: commodity avg `0.2241` n `12`; crypto_alt avg `0.089` n `228`; crypto_major avg `-0.0099` n `8`; equity avg `0.1189` n `65`; fx avg `-0.0275` n `4`; index avg `0.0848` n `23`; metal avg `-0.2115` n `18`; unknown avg `-0.3649` n `356`
- 4h: commodity avg `-0.3548` n `12`; crypto_alt avg `-0.1743` n `228`; crypto_major avg `-0.7893` n `8`; equity avg `0.579` n `65`; fx avg `-0.0388` n `4`; index avg `0.4777` n `23`; metal avg `0.2844` n `18`; unknown avg `0.5108` n `356`
- 24h: commodity avg `-2.3868` n `7`; crypto_alt avg `3.0589` n `223`; crypto_major avg `1.0719` n `7`; equity avg `2.4111` n `47`; fx avg `-0.4683` n `4`; index avg `1.8603` n `6`; metal avg `2.9978` n `7`; unknown avg `4.0899` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1545`, n `469`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1442`, n `465`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `469`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1275`, n `465`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `469`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `469`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1098`, n `465`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `469`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0953`, n `465`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `465`, weak_sample_signal
