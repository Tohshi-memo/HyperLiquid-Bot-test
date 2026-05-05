# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T01:15:17.800391+00:00`
- Correlation status: `ready`
- Asset price records: `315`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `7`; crypto_alt avg `0.2572` n `223`; crypto_major avg `0.1079` n `7`; equity avg `0.148` n `47`; fx avg `-0.0038` n `4`; index avg `0.0247` n `6`; metal avg `0.1976` n `7`; unknown avg `-0.0653` n `312`
- 1h: commodity avg `0.0357` n `7`; crypto_alt avg `0.4432` n `223`; crypto_major avg `0.3588` n `7`; equity avg `0.3155` n `47`; fx avg `-0.0067` n `4`; index avg `0.0375` n `6`; metal avg `0.3223` n `7`; unknown avg `-0.0164` n `312`
- 4h: commodity avg `-0.0962` n `7`; crypto_alt avg `0.3632` n `223`; crypto_major avg `0.226` n `7`; equity avg `0.2753` n `47`; fx avg `-0.0075` n `4`; index avg `-0.1179` n `6`; metal avg `0.3265` n `7`; unknown avg `-0.0458` n `312`
- 24h: commodity avg `1.3342` n `7`; crypto_alt avg `2.3073` n `223`; crypto_major avg `1.4603` n `7`; equity avg `-0.2757` n `47`; fx avg `-0.0404` n `4`; index avg `-0.0369` n `6`; metal avg `-1.5778` n `7`; unknown avg `-1.3969` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2328`, n `311`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2267`, n `311`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1617`, n `307`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1597`, n `307`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1514`, n `311`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `311`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1403`, n `311`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `311`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `307`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1189`, n `311`, weak_sample_signal
