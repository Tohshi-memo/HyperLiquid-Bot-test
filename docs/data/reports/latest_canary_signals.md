# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T13:22:28.452053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8678` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6762` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0299` n `12`; crypto_alt avg `-0.1298` n `228`; crypto_major avg `-0.0132` n `8`; equity avg `-0.02` n `86`; fx avg `-0.0058` n `6`; index avg `-0.0052` n `23`; metal avg `0.0165` n `20`; unknown avg `0.1187` n `765`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.8226` n `228`; crypto_major avg `-0.8558` n `8`; equity avg `-0.5204` n `86`; fx avg `0.0298` n `6`; index avg `-0.0857` n `23`; metal avg `0.025` n `20`; unknown avg `-0.0112` n `765`
- 4h: commodity avg `0.1043` n `12`; crypto_alt avg `-1.5377` n `228`; crypto_major avg `-1.756` n `8`; equity avg `-0.6436` n `86`; fx avg `0.0381` n `6`; index avg `-0.0798` n `23`; metal avg `0.1118` n `20`; unknown avg `-0.0917` n `765`
- 24h: commodity avg `-0.0531` n `12`; crypto_alt avg `-2.6767` n `228`; crypto_major avg `-2.8244` n `8`; equity avg `-4.7551` n `86`; fx avg `0.0669` n `6`; index avg `-0.7202` n `23`; metal avg `0.1774` n `20`; unknown avg `0.6308` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3331`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
