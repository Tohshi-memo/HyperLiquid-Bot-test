# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T20:45:09.877804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `-0.1852` n `230`; crypto_major avg `-0.1633` n `8`; equity avg `-0.0066` n `92`; fx avg `0.0012` n `6`; index avg `-0.0075` n `25`; metal avg `0.0067` n `20`; unknown avg `-0.0954` n `766`
- 1h: commodity avg `0.1123` n `12`; crypto_alt avg `-0.4152` n `230`; crypto_major avg `-0.3853` n `8`; equity avg `-0.1658` n `92`; fx avg `-0.0205` n `6`; index avg `-0.0737` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.2161` n `766`
- 4h: commodity avg `0.4925` n `12`; crypto_alt avg `-0.8489` n `230`; crypto_major avg `-0.4308` n `8`; equity avg `-0.3418` n `92`; fx avg `-0.0307` n `6`; index avg `-0.1075` n `25`; metal avg `0.0173` n `20`; unknown avg `-0.4149` n `766`
- 24h: commodity avg `0.6794` n `12`; crypto_alt avg `-2.5691` n `230`; crypto_major avg `-3.204` n `8`; equity avg `-3.3411` n `92`; fx avg `-0.0791` n `6`; index avg `-0.6858` n `25`; metal avg `-0.5524` n `20`; unknown avg `-0.3366` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
