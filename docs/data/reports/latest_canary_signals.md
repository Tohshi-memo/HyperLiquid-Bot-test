# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T03:52:29.136463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.929` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5498` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0821` n `13`; crypto_alt avg `-0.0737` n `236`; crypto_major avg `-0.031` n `8`; equity avg `-0.2125` n `151`; fx avg `0.0021` n `6`; index avg `-0.0306` n `26`; metal avg `-0.0516` n `20`; unknown avg `2.0591` n `1136`
- 1h: commodity avg `-0.0385` n `13`; crypto_alt avg `-0.5919` n `236`; crypto_major avg `-0.5025` n `8`; equity avg `-0.3662` n `151`; fx avg `-0.0511` n `6`; index avg `-0.0481` n `26`; metal avg `-0.0838` n `20`; unknown avg `-0.3523` n `1134`
- 4h: commodity avg `-0.2924` n `13`; crypto_alt avg `-3.2753` n `236`; crypto_major avg `-1.8016` n `8`; equity avg `-0.5753` n `151`; fx avg `0.1433` n `6`; index avg `-0.2518` n `26`; metal avg `0.1274` n `20`; unknown avg `-0.1884` n `1128`
- 24h: commodity avg `-0.4757` n `13`; crypto_alt avg `-6.0137` n `236`; crypto_major avg `-4.4214` n `8`; equity avg `-6.4357` n `151`; fx avg `0.0822` n `6`; index avg `-1.0979` n `26`; metal avg `-0.7559` n `20`; unknown avg `1393.4964` n `890`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1471`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1201`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1048`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1027`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0982`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0955`, n `666`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0815`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0786`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0687`, n `666`, weak_sample_signal
