# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T00:00:30.656891+00:00`
- Correlation status: `ready`
- Asset price records: `215`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1234` n `7`; crypto_alt avg `-0.1002` n `223`; crypto_major avg `-0.1111` n `7`; equity avg `-0.0019` n `42`; fx avg `0.0053` n `4`; index avg `0.1775` n `9`; metal avg `-0.0396` n `7`; unknown avg `0.0019` n `314`
- 1h: commodity avg `0.3638` n `7`; crypto_alt avg `-0.6306` n `223`; crypto_major avg `-0.8179` n `7`; equity avg `-0.2602` n `42`; fx avg `-0.0011` n `4`; index avg `0.0508` n `9`; metal avg `-0.1135` n `7`; unknown avg `0.4013` n `314`
- 4h: commodity avg `0.3081` n `7`; crypto_alt avg `-0.4578` n `223`; crypto_major avg `-0.3736` n `7`; equity avg `-0.2594` n `42`; fx avg `-0.0465` n `4`; index avg `0.0232` n `9`; metal avg `-0.19` n `7`; unknown avg `0.1219` n `314`
- 24h: commodity avg `0.1643` n `7`; crypto_alt avg `-0.6176` n `223`; crypto_major avg `-0.1681` n `7`; equity avg `-0.1026` n `42`; fx avg `-0.0287` n `4`; index avg `0.0989` n `9`; metal avg `0.279` n `7`; unknown avg `-0.0256` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3899`, n `211`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.373`, n `211`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2964`, n `211`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2859`, n `211`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2814`, n `207`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.281`, n `207`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2807`, n `207`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2758`, n `207`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2496`, n `211`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2457`, n `211`, weak_sample_signal
