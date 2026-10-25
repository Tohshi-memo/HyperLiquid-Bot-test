# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T16:52:53.116177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `13`; crypto_alt avg `0.202` n `237`; crypto_major avg `0.1684` n `8`; equity avg `0.0402` n `152`; fx avg `0.0055` n `6`; index avg `0.0009` n `26`; metal avg `0.0195` n `20`; unknown avg `3.756` n `1240`
- 1h: commodity avg `-0.0278` n `13`; crypto_alt avg `-0.0839` n `237`; crypto_major avg `0.0096` n `8`; equity avg `0.1239` n `152`; fx avg `-0.0082` n `6`; index avg `0.0148` n `26`; metal avg `0.0331` n `20`; unknown avg `2.572` n `1234`
- 4h: commodity avg `-0.0639` n `13`; crypto_alt avg `0.5896` n `237`; crypto_major avg `0.4297` n `8`; equity avg `0.3893` n `152`; fx avg `-0.0096` n `6`; index avg `0.0511` n `26`; metal avg `0.073` n `20`; unknown avg `124.4426` n `1225`
- 24h: commodity avg `-0.1829` n `13`; crypto_alt avg `0.626` n `237`; crypto_major avg `1.2292` n `8`; equity avg `0.7769` n `152`; fx avg `0.0155` n `6`; index avg `0.1425` n `26`; metal avg `0.1553` n `20`; unknown avg `9.4952` n `1083`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2247`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
