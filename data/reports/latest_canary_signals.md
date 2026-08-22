# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T08:12:57.371824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6543` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6051` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0123` n `12`; crypto_alt avg `0.4322` n `230`; crypto_major avg `0.0386` n `8`; equity avg `-0.0621` n `121`; fx avg `0.0015` n `6`; index avg `-0.0126` n `25`; metal avg `0.0014` n `20`; unknown avg `0.2897` n `794`
- 1h: commodity avg `-0.0113` n `12`; crypto_alt avg `-0.2102` n `230`; crypto_major avg `-0.614` n `8`; equity avg `-0.1251` n `121`; fx avg `0.0002` n `6`; index avg `-0.0304` n `25`; metal avg `0.0173` n `20`; unknown avg `0.283` n `794`
- 4h: commodity avg `0.0597` n `12`; crypto_alt avg `-3.2347` n `230`; crypto_major avg `-1.7015` n `8`; equity avg `-0.4185` n `121`; fx avg `-0.0014` n `6`; index avg `-0.0472` n `25`; metal avg `-0.0964` n `20`; unknown avg `0.1674` n `778`
- 24h: commodity avg `0.0272` n `12`; crypto_alt avg `5.3931` n `230`; crypto_major avg `6.0404` n `8`; equity avg `-0.595` n `121`; fx avg `0.054` n `6`; index avg `-0.1193` n `25`; metal avg `-0.0509` n `20`; unknown avg `2.0441` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
