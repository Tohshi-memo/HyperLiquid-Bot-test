# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T23:45:17.686936+00:00`
- Correlation status: `ready`
- Asset price records: `214`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0439` n `7`; crypto_alt avg `-0.0294` n `223`; crypto_major avg `-0.0731` n `7`; equity avg `-0.0584` n `42`; fx avg `-0.0088` n `4`; index avg `-0.1972` n `9`; metal avg `-0.0918` n `7`; unknown avg `0.0099` n `314`
- 1h: commodity avg `0.3676` n `7`; crypto_alt avg `-0.7407` n `223`; crypto_major avg `-0.8467` n `7`; equity avg `-0.4419` n `42`; fx avg `-0.0104` n `4`; index avg `-0.1415` n `9`; metal avg `-0.2238` n `7`; unknown avg `0.282` n `314`
- 4h: commodity avg `0.2022` n `7`; crypto_alt avg `-0.4638` n `223`; crypto_major avg `-0.3126` n `7`; equity avg `-0.276` n `42`; fx avg `-0.0622` n `4`; index avg `-0.1571` n `9`; metal avg `-0.1182` n `7`; unknown avg `0.0343` n `314`
- 24h: commodity avg `0.0259` n `7`; crypto_alt avg `-0.674` n `223`; crypto_major avg `-0.1337` n `7`; equity avg `-0.1421` n `42`; fx avg `-0.0297` n `4`; index avg `-0.0763` n `9`; metal avg `0.3328` n `7`; unknown avg `0.1702` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3901`, n `210`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3731`, n `210`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3043`, n `210`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2937`, n `210`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2767`, n `206`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2764`, n `206`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2689`, n `206`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2641`, n `210`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2635`, n `206`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2625`, n `210`, moderate_sample_signal
