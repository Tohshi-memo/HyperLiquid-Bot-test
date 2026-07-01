# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T03:37:29.874944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.49` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5645` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `0.4803` n `228`; crypto_major avg `0.5308` n `8`; equity avg `0.1012` n `88`; fx avg `0.0003` n `6`; index avg `0.0411` n `23`; metal avg `-0.0219` n `20`; unknown avg `0.2191` n `765`
- 1h: commodity avg `0.0169` n `12`; crypto_alt avg `0.4786` n `228`; crypto_major avg `0.3781` n `8`; equity avg `0.3077` n `88`; fx avg `0.0205` n `6`; index avg `0.0581` n `23`; metal avg `-0.0353` n `20`; unknown avg `-0.1254` n `765`
- 4h: commodity avg `-0.0716` n `12`; crypto_alt avg `1.0368` n `228`; crypto_major avg `1.0672` n `8`; equity avg `-0.4973` n `88`; fx avg `0.0905` n `6`; index avg `-0.1948` n `23`; metal avg `-0.3641` n `20`; unknown avg `0.7457` n `765`
- 24h: commodity avg `0.0765` n `12`; crypto_alt avg `-0.6486` n `228`; crypto_major avg `-0.1593` n `8`; equity avg `0.6131` n `88`; fx avg `0.1801` n `6`; index avg `0.0222` n `23`; metal avg `-0.0104` n `20`; unknown avg `6.5079` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
