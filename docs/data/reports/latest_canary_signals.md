# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T14:22:41.918820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `0.0821` n `230`; crypto_major avg `0.1562` n `8`; equity avg `-0.2714` n `114`; fx avg `0.006` n `6`; index avg `-0.0354` n `25`; metal avg `-0.0266` n `20`; unknown avg `-0.0819` n `795`
- 1h: commodity avg `-0.0977` n `12`; crypto_alt avg `0.0746` n `230`; crypto_major avg `0.3222` n `8`; equity avg `-0.6572` n `114`; fx avg `0.029` n `6`; index avg `-0.073` n `25`; metal avg `-0.0348` n `20`; unknown avg `-0.0644` n `795`
- 4h: commodity avg `0.0126` n `12`; crypto_alt avg `0.2263` n `230`; crypto_major avg `0.304` n `8`; equity avg `-0.6556` n `114`; fx avg `0.0429` n `6`; index avg `-0.0529` n `25`; metal avg `-0.1065` n `20`; unknown avg `-0.0242` n `795`
- 24h: commodity avg `0.4995` n `12`; crypto_alt avg `-0.5283` n `230`; crypto_major avg `0.3635` n `8`; equity avg `-3.324` n `114`; fx avg `-0.0302` n `6`; index avg `-0.6054` n `25`; metal avg `-0.4165` n `20`; unknown avg `-0.1284` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
