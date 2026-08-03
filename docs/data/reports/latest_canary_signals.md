# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T16:22:30.314234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7327` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0428` n `12`; crypto_alt avg `0.0538` n `230`; crypto_major avg `0.1993` n `8`; equity avg `0.2146` n `103`; fx avg `-0.0059` n `6`; index avg `0.0233` n `25`; metal avg `-0.0206` n `20`; unknown avg `-0.0938` n `784`
- 1h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.1551` n `230`; crypto_major avg `0.3317` n `8`; equity avg `0.4911` n `103`; fx avg `0.0074` n `6`; index avg `0.0802` n `25`; metal avg `-0.0362` n `20`; unknown avg `-0.1679` n `784`
- 4h: commodity avg `0.0907` n `12`; crypto_alt avg `1.022` n `230`; crypto_major avg `1.6212` n `8`; equity avg `2.774` n `103`; fx avg `-0.0086` n `6`; index avg `0.2401` n `25`; metal avg `-0.1115` n `20`; unknown avg `0.08` n `784`
- 24h: commodity avg `-0.1395` n `12`; crypto_alt avg `0.395` n `230`; crypto_major avg `1.4471` n `8`; equity avg `1.8106` n `102`; fx avg `-0.1685` n `6`; index avg `0.0254` n `25`; metal avg `-0.4827` n `20`; unknown avg `0.1184` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
