# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T15:21:51.233693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `0.018` n `230`; crypto_major avg `0.0206` n `8`; equity avg `-0.1689` n `103`; fx avg `0.0137` n `6`; index avg `-0.0384` n `25`; metal avg `0.029` n `20`; unknown avg `-0.0947` n `784`
- 1h: commodity avg `0.1351` n `12`; crypto_alt avg `0.2106` n `230`; crypto_major avg `0.6087` n `8`; equity avg `0.7862` n `103`; fx avg `0.0274` n `6`; index avg `0.0892` n `25`; metal avg `0.0811` n `20`; unknown avg `-0.1981` n `784`
- 4h: commodity avg `0.0265` n `12`; crypto_alt avg `0.8749` n `230`; crypto_major avg `1.1607` n `8`; equity avg `1.9609` n `103`; fx avg `-0.0279` n `6`; index avg `0.0944` n `25`; metal avg `-0.1643` n `20`; unknown avg `0.0525` n `784`
- 24h: commodity avg `-0.2254` n `12`; crypto_alt avg `0.1368` n `230`; crypto_major avg `1.0024` n `8`; equity avg `1.2773` n `102`; fx avg `-0.1779` n `6`; index avg `-0.0454` n `25`; metal avg `-0.4388` n `20`; unknown avg `0.1549` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
