# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T08:22:33.305451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `12`; crypto_alt avg `-0.2135` n `229`; crypto_major avg `-0.305` n `8`; equity avg `-0.1614` n `88`; fx avg `0.0009` n `6`; index avg `-0.0238` n `25`; metal avg `-0.101` n `20`; unknown avg `-0.0814` n `765`
- 1h: commodity avg `-0.1676` n `12`; crypto_alt avg `-0.0397` n `229`; crypto_major avg `0.0005` n `8`; equity avg `-0.0043` n `88`; fx avg `-0.0181` n `6`; index avg `0.0134` n `25`; metal avg `0.0816` n `20`; unknown avg `-0.0326` n `765`
- 4h: commodity avg `-0.0434` n `12`; crypto_alt avg `-0.6688` n `229`; crypto_major avg `-0.5096` n `8`; equity avg `0.1986` n `88`; fx avg `0.0148` n `6`; index avg `0.1029` n `25`; metal avg `0.1423` n `20`; unknown avg `-0.2361` n `731`
- 24h: commodity avg `-0.2725` n `12`; crypto_alt avg `-0.252` n `229`; crypto_major avg `0.7371` n `8`; equity avg `-0.6343` n `88`; fx avg `0.0781` n `6`; index avg `0.002` n `25`; metal avg `-0.106` n `20`; unknown avg `1.1055` n `661`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
