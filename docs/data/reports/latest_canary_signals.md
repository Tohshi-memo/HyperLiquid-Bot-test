# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T16:15:18.410500+00:00`
- Correlation status: `ready`
- Asset price records: `279`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1431` n `7`; crypto_alt avg `-0.1198` n `223`; crypto_major avg `-0.1861` n `7`; equity avg `-0.6137` n `42`; fx avg `-0.0305` n `4`; index avg `0.075` n `9`; metal avg `-0.3947` n `7`; unknown avg `0.0091` n `314`
- 1h: commodity avg `0.4688` n `7`; crypto_alt avg `-0.7048` n `223`; crypto_major avg `-0.8952` n `7`; equity avg `-1.5053` n `42`; fx avg `-0.0282` n `4`; index avg `-0.2467` n `9`; metal avg `-0.8758` n `7`; unknown avg `-0.3573` n `314`
- 4h: commodity avg `1.0683` n `7`; crypto_alt avg `0.2604` n `223`; crypto_major avg `0.1403` n `7`; equity avg `-0.6891` n `42`; fx avg `-0.0177` n `4`; index avg `0.3452` n `9`; metal avg `-0.8125` n `7`; unknown avg `-0.5732` n `314`
- 24h: commodity avg `2.1839` n `7`; crypto_alt avg `1.4256` n `223`; crypto_major avg `0.7086` n `7`; equity avg `-0.4254` n `42`; fx avg `-0.1062` n `4`; index avg `0.7668` n `9`; metal avg `-2.5204` n `7`; unknown avg `-0.7888` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2356`, n `276`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2302`, n `276`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1766`, n `272`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1763`, n `272`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1571`, n `272`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.156`, n `272`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1556`, n `272`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1542`, n `272`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `276`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1491`, n `276`, weak_sample_signal
