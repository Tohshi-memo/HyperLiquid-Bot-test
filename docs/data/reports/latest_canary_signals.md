# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T01:52:29.004615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7623` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6676` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0745` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0134` n `13`; crypto_alt avg `-0.7913` n `238`; crypto_major avg `-0.7241` n `8`; equity avg `-0.4662` n `155`; fx avg `-0.0132` n `6`; index avg `-0.0816` n `27`; metal avg `-0.0283` n `20`; unknown avg `1.3435` n `1238`
- 1h: commodity avg `0.0687` n `13`; crypto_alt avg `-1.4725` n `238`; crypto_major avg `-1.2998` n `8`; equity avg `-1.1864` n `155`; fx avg `-0.0387` n `6`; index avg `-0.2253` n `27`; metal avg `0.0461` n `20`; unknown avg `2.0248` n `1232`
- 4h: commodity avg `0.0311` n `13`; crypto_alt avg `-2.2942` n `238`; crypto_major avg `-1.848` n `8`; equity avg `-1.0384` n `155`; fx avg `-0.1437` n `6`; index avg `-0.1804` n `27`; metal avg `-0.0857` n `20`; unknown avg `2.5209` n `1150`
- 24h: commodity avg `-0.006` n `13`; crypto_alt avg `-1.6171` n `238`; crypto_major avg `-1.3375` n `8`; equity avg `-0.9846` n `154`; fx avg `-0.0014` n `6`; index avg `-0.1651` n `27`; metal avg `-0.1455` n `20`; unknown avg `27.5299` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
