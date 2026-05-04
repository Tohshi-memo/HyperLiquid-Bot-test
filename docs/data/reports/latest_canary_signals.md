# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T19:45:23.346223+00:00`
- Correlation status: `ready`
- Asset price records: `293`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0541` n `7`; crypto_alt avg `-0.1418` n `223`; crypto_major avg `-0.0685` n `7`; equity avg `-0.0102` n `42`; fx avg `0.0024` n `4`; index avg `-0.0078` n `9`; metal avg `-0.0208` n `7`; unknown avg `-0.03` n `314`
- 1h: commodity avg `-0.1674` n `7`; crypto_alt avg `-0.3415` n `223`; crypto_major avg `-0.2394` n `7`; equity avg `0.0317` n `42`; fx avg `0.0007` n `4`; index avg `0.0652` n `9`; metal avg `0.1782` n `7`; unknown avg `-0.1282` n `314`
- 4h: commodity avg `0.0126` n `7`; crypto_alt avg `0.4436` n `223`; crypto_major avg `0.1617` n `7`; equity avg `-0.4314` n `42`; fx avg `-0.0178` n `4`; index avg `-0.1535` n `9`; metal avg `-0.0485` n `7`; unknown avg `0.0949` n `314`
- 24h: commodity avg `1.6513` n `7`; crypto_alt avg `1.48` n `223`; crypto_major avg `0.7143` n `7`; equity avg `-0.3647` n `42`; fx avg `-0.0798` n `4`; index avg `0.5076` n `9`; metal avg `-2.3077` n `7`; unknown avg `-1.045` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2364`, n `289`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2305`, n `289`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1693`, n `285`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1682`, n `285`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1504`, n `289`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `289`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1434`, n `289`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `289`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1269`, n `285`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1222`, n `285`, weak_sample_signal
