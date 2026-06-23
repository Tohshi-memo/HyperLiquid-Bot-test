# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T11:37:26.839060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0207` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `0.1114` n `228`; crypto_major avg `-0.0172` n `8`; equity avg `0.0067` n `86`; fx avg `-0.0099` n `6`; index avg `0.0015` n `23`; metal avg `-0.0916` n `20`; unknown avg `0.1302` n `764`
- 1h: commodity avg `-0.0354` n `12`; crypto_alt avg `0.6248` n `228`; crypto_major avg `0.4821` n `8`; equity avg `0.4125` n `86`; fx avg `-0.0083` n `6`; index avg `0.0235` n `23`; metal avg `-0.145` n `20`; unknown avg `0.2029` n `764`
- 4h: commodity avg `0.1113` n `12`; crypto_alt avg `-0.6321` n `228`; crypto_major avg `-1.0964` n `8`; equity avg `-0.0948` n `86`; fx avg `-0.0614` n `6`; index avg `-0.0757` n `23`; metal avg `-0.0785` n `20`; unknown avg `-0.3162` n `764`
- 24h: commodity avg `-0.5036` n `12`; crypto_alt avg `-4.1585` n `228`; crypto_major avg `-4.4364` n `8`; equity avg `-4.331` n `85`; fx avg `-0.1336` n `6`; index avg `-0.9378` n `23`; metal avg `-1.3481` n `20`; unknown avg `-0.0189` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
