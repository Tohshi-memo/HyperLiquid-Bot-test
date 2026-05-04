# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T19:53:14.151541+00:00`
- Correlation status: `ready`
- Asset price records: `293`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `7`; crypto_alt avg `-0.1345` n `223`; crypto_major avg `-0.045` n `7`; equity avg `-0.0825` n `42`; fx avg `-0.0051` n `4`; index avg `-0.0194` n `9`; metal avg `-0.0471` n `7`; unknown avg `-0.1404` n `314`
- 1h: commodity avg `-0.1994` n `7`; crypto_alt avg `-0.3339` n `223`; crypto_major avg `-0.216` n `7`; equity avg `-0.0407` n `42`; fx avg `-0.0068` n `4`; index avg `0.0538` n `9`; metal avg `0.1518` n `7`; unknown avg `-0.2402` n `314`
- 4h: commodity avg `-0.0196` n `7`; crypto_alt avg `0.4515` n `223`; crypto_major avg `0.1853` n `7`; equity avg `-0.5035` n `42`; fx avg `-0.0252` n `4`; index avg `-0.1649` n `9`; metal avg `-0.0748` n `7`; unknown avg `-0.0454` n `314`
- 24h: commodity avg `1.6178` n `7`; crypto_alt avg `1.4883` n `223`; crypto_major avg `0.7381` n `7`; equity avg `-0.4364` n `42`; fx avg `-0.0873` n `4`; index avg `0.4967` n `9`; metal avg `-2.3331` n `7`; unknown avg `-1.12` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2365`, n `289`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2306`, n `289`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.171`, n `285`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1699`, n `285`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1504`, n `289`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `289`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1434`, n `289`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `289`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1267`, n `285`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1217`, n `285`, weak_sample_signal
