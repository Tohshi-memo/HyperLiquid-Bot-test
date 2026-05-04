# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T00:07:07.940800+00:00`
- Correlation status: `ready`
- Asset price records: `215`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0464` n `7`; crypto_alt avg `-0.0683` n `223`; crypto_major avg `-0.0502` n `7`; equity avg `0.11` n `42`; fx avg `0.0106` n `4`; index avg `0.2624` n `9`; metal avg `0.0451` n `7`; unknown avg `-0.039` n `314`
- 1h: commodity avg `0.2864` n `7`; crypto_alt avg `-0.5986` n `223`; crypto_major avg `-0.7573` n `7`; equity avg `-0.1496` n `42`; fx avg `0.0042` n `4`; index avg `0.136` n `9`; metal avg `-0.029` n `7`; unknown avg `0.3253` n `314`
- 4h: commodity avg `0.2304` n `7`; crypto_alt avg `-0.4249` n `223`; crypto_major avg `-0.3127` n `7`; equity avg `-0.1484` n `42`; fx avg `-0.0412` n `4`; index avg `0.1085` n `9`; metal avg `-0.1056` n `7`; unknown avg `0.0758` n `314`
- 24h: commodity avg `0.0866` n `7`; crypto_alt avg `-0.5812` n `223`; crypto_major avg `-0.107` n `7`; equity avg `0.0106` n `42`; fx avg `-0.0233` n `4`; index avg `0.1842` n `9`; metal avg `0.364` n `7`; unknown avg `-0.0548` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3901`, n `211`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3732`, n `211`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2976`, n `211`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2882`, n `207`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2876`, n `207`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2871`, n `211`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2768`, n `207`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2717`, n `207`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2504`, n `211`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2467`, n `211`, weak_sample_signal
