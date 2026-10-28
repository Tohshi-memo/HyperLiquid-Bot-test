# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T22:07:39.930754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `13`; crypto_alt avg `-0.4217` n `238`; crypto_major avg `-0.2197` n `8`; equity avg `0.0022` n `155`; fx avg `0.0026` n `6`; index avg `-0.0127` n `27`; metal avg `0.0271` n `20`; unknown avg `0.3116` n `1232`
- 1h: commodity avg `0.0288` n `13`; crypto_alt avg `-0.2967` n `238`; crypto_major avg `-0.108` n `8`; equity avg `-0.1647` n `155`; fx avg `-0.0017` n `6`; index avg `-0.0215` n `27`; metal avg `0.0297` n `20`; unknown avg `3.563` n `1232`
- 4h: commodity avg `-0.2879` n `13`; crypto_alt avg `1.1902` n `238`; crypto_major avg `0.7181` n `8`; equity avg `-0.0765` n `155`; fx avg `-0.0137` n `6`; index avg `-0.0525` n `27`; metal avg `0.1773` n `20`; unknown avg `5.2185` n `1112`
- 24h: commodity avg `0.176` n `13`; crypto_alt avg `0.8017` n `238`; crypto_major avg `0.6683` n `8`; equity avg `1.07` n `154`; fx avg `0.2428` n `6`; index avg `0.1728` n `27`; metal avg `-0.084` n `20`; unknown avg `24.5786` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
