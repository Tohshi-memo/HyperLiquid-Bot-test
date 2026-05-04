# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T01:00:32.958970+00:00`
- Correlation status: `ready`
- Asset price records: `219`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1238` n `7`; crypto_alt avg `0.5495` n `223`; crypto_major avg `0.3877` n `7`; equity avg `0.1968` n `42`; fx avg `0.0021` n `4`; index avg `0.0458` n `9`; metal avg `0.1025` n `7`; unknown avg `0.0148` n `314`
- 1h: commodity avg `-0.1844` n `7`; crypto_alt avg `0.3003` n `223`; crypto_major avg `0.1142` n `7`; equity avg `0.2658` n `42`; fx avg `-0.0005` n `4`; index avg `-0.0142` n `9`; metal avg `-0.1405` n `7`; unknown avg `-0.009` n `314`
- 4h: commodity avg `0.6078` n `7`; crypto_alt avg `-0.2027` n `223`; crypto_major avg `-0.2001` n `7`; equity avg `0.0917` n `42`; fx avg `-0.0372` n `4`; index avg `0.0524` n `9`; metal avg `-0.2429` n `7`; unknown avg `0.2301` n `314`
- 24h: commodity avg `-0.1005` n `7`; crypto_alt avg `-0.0226` n `223`; crypto_major avg `0.2452` n `7`; equity avg `0.2666` n `42`; fx avg `-0.0196` n `4`; index avg `0.1456` n `9`; metal avg `0.2545` n `7`; unknown avg `0.2853` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3858`, n `215`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3695`, n `215`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3118`, n `211`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3109`, n `211`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2892`, n `215`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2786`, n `215`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2426`, n `211`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2376`, n `211`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2278`, n `215`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2143`, n `215`, weak_sample_signal
