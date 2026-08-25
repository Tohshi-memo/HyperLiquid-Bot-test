# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T03:37:59.674738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.5987` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1646` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.5347` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0396` n `12`; crypto_alt avg `0.1085` n `231`; crypto_major avg `0.0907` n `8`; equity avg `0.1783` n `122`; fx avg `-0.0068` n `6`; index avg `0.008` n `25`; metal avg `0.0602` n `20`; unknown avg `-0.028` n `794`
- 1h: commodity avg `-0.0538` n `12`; crypto_alt avg `0.1056` n `231`; crypto_major avg `0.065` n `8`; equity avg `0.2419` n `122`; fx avg `0.0021` n `6`; index avg `0.04` n `25`; metal avg `-0.055` n `20`; unknown avg `1.1028` n `794`
- 4h: commodity avg `0.0799` n `12`; crypto_alt avg `1.787` n `231`; crypto_major avg `2.2445` n `8`; equity avg `0.7098` n `122`; fx avg `0.0212` n `6`; index avg `0.0823` n `25`; metal avg `-0.3542` n `20`; unknown avg `0.3481` n `794`
- 24h: commodity avg `0.0549` n `12`; crypto_alt avg `2.5663` n `231`; crypto_major avg `3.3736` n `8`; equity avg `-0.5134` n `122`; fx avg `0.022` n `6`; index avg `-0.1003` n `25`; metal avg `-0.1968` n `20`; unknown avg `0.641` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
