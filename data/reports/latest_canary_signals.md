# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T01:52:26.534709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5777` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.0243` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `0.3111` n `229`; crypto_major avg `0.4034` n `8`; equity avg `0.0814` n `91`; fx avg `-0.0324` n `6`; index avg `0.0235` n `25`; metal avg `0.0406` n `20`; unknown avg `0.1593` n `763`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `-1.1218` n `229`; crypto_major avg `-0.9897` n `8`; equity avg `-0.3377` n `91`; fx avg `-0.0651` n `6`; index avg `-0.1043` n `25`; metal avg `-0.1243` n `20`; unknown avg `-0.054` n `763`
- 4h: commodity avg `-0.0704` n `12`; crypto_alt avg `-0.8042` n `229`; crypto_major avg `-0.9135` n `8`; equity avg `0.6642` n `91`; fx avg `-0.0006` n `6`; index avg `0.1108` n `25`; metal avg `-0.1225` n `20`; unknown avg `-0.2575` n `763`
- 24h: commodity avg `0.8028` n `12`; crypto_alt avg `-3.1462` n `229`; crypto_major avg `-2.5109` n `8`; equity avg `-2.044` n `91`; fx avg `-0.2123` n `6`; index avg `-0.2695` n `25`; metal avg `-0.5351` n `20`; unknown avg `-0.3147` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
