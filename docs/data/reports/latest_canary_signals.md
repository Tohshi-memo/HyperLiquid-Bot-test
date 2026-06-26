# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T08:37:36.862320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0972` n `12`; crypto_alt avg `-0.1625` n `228`; crypto_major avg `-0.2208` n `8`; equity avg `-0.0955` n `86`; fx avg `0.0208` n `6`; index avg `-0.0115` n `23`; metal avg `0.0267` n `20`; unknown avg `0.013` n `765`
- 1h: commodity avg `-0.1723` n `12`; crypto_alt avg `-0.4923` n `228`; crypto_major avg `-0.6846` n `8`; equity avg `-0.1972` n `86`; fx avg `0.0321` n `6`; index avg `-0.0307` n `23`; metal avg `-0.0089` n `20`; unknown avg `0.0013` n `765`
- 4h: commodity avg `-0.143` n `12`; crypto_alt avg `1.0263` n `228`; crypto_major avg `1.0674` n `8`; equity avg `0.6185` n `86`; fx avg `-0.0276` n `6`; index avg `0.1795` n `23`; metal avg `0.6581` n `20`; unknown avg `0.419` n `733`
- 24h: commodity avg `0.0489` n `12`; crypto_alt avg `-1.8115` n `228`; crypto_major avg `-1.6563` n `8`; equity avg `-3.8808` n `86`; fx avg `0.0446` n `6`; index avg `-0.565` n `23`; metal avg `0.3991` n `20`; unknown avg `0.5796` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
