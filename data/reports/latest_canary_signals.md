# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T15:52:31.874182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `0.5164` n `234`; crypto_major avg `0.6827` n `8`; equity avg `0.0672` n `140`; fx avg `-0.0013` n `6`; index avg `0.0181` n `26`; metal avg `-0.033` n `20`; unknown avg `4.2281` n `942`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `-0.221` n `234`; crypto_major avg `0.3167` n `8`; equity avg `0.3929` n `140`; fx avg `0.0019` n `6`; index avg `0.0875` n `26`; metal avg `0.0017` n `20`; unknown avg `5.8617` n `940`
- 4h: commodity avg `-0.1633` n `12`; crypto_alt avg `0.2214` n `234`; crypto_major avg `1.1974` n `8`; equity avg `0.8708` n `140`; fx avg `-0.0041` n `6`; index avg `0.2064` n `26`; metal avg `-0.1572` n `20`; unknown avg `13.1217` n `876`
- 24h: commodity avg `-1.0144` n `12`; crypto_alt avg `6.4464` n `234`; crypto_major avg `6.5745` n `8`; equity avg `2.7787` n `140`; fx avg `-0.0966` n `6`; index avg `0.5786` n `26`; metal avg `0.0261` n `20`; unknown avg `4.5464` n `707`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
