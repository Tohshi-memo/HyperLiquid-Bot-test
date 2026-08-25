# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T09:48:16.507884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7501` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2993` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `0.01` n `231`; crypto_major avg `-0.1088` n `8`; equity avg `0.0981` n `122`; fx avg `-0.0023` n `6`; index avg `0.0083` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.0366` n `794`
- 1h: commodity avg `-0.2022` n `12`; crypto_alt avg `0.2979` n `231`; crypto_major avg `0.1858` n `8`; equity avg `0.4273` n `122`; fx avg `-0.0125` n `6`; index avg `0.0797` n `25`; metal avg `0.093` n `20`; unknown avg `0.0104` n `794`
- 4h: commodity avg `-0.4453` n `12`; crypto_alt avg `-1.1394` n `231`; crypto_major avg `-1.1626` n `8`; equity avg `0.5875` n `122`; fx avg `0.0232` n `6`; index avg `0.1367` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.2968` n `778`
- 24h: commodity avg `-0.6944` n `12`; crypto_alt avg `0.9607` n `231`; crypto_major avg `1.8994` n `8`; equity avg `0.6304` n `122`; fx avg `0.0515` n `6`; index avg `0.12` n `25`; metal avg `-0.1993` n `20`; unknown avg `-0.112` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
