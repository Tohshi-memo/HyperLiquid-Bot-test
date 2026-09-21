# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T20:22:26.143023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `12`; crypto_alt avg `0.3608` n `234`; crypto_major avg `0.6669` n `8`; equity avg `-0.0523` n `140`; fx avg `-0.0036` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0078` n `20`; unknown avg `3.2003` n `912`
- 1h: commodity avg `-0.0875` n `12`; crypto_alt avg `0.8169` n `234`; crypto_major avg `0.9656` n `8`; equity avg `-0.1148` n `140`; fx avg `-0.0053` n `6`; index avg `-0.0442` n `26`; metal avg `-0.023` n `20`; unknown avg `13.0307` n `874`
- 4h: commodity avg `0.0536` n `12`; crypto_alt avg `-0.1359` n `234`; crypto_major avg `1.3132` n `8`; equity avg `0.1899` n `140`; fx avg `0.0061` n `6`; index avg `0.0419` n `26`; metal avg `-0.0588` n `20`; unknown avg `4.4678` n `874`
- 24h: commodity avg `-1.057` n `12`; crypto_alt avg `4.1636` n `234`; crypto_major avg `6.3322` n `8`; equity avg `2.8155` n `140`; fx avg `-0.0714` n `6`; index avg `0.6237` n `26`; metal avg `0.0396` n `20`; unknown avg `15.2612` n `699`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
