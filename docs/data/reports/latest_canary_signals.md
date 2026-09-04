# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T12:37:27.727150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.3403` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.1623` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.8548` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7203` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0314` n `12`; crypto_alt avg `-1.9248` n `232`; crypto_major avg `-2.1464` n `8`; equity avg `-0.8526` n `133`; fx avg `-0.0168` n `6`; index avg `-0.096` n `26`; metal avg `-0.486` n `20`; unknown avg `1.9734` n `787`
- 1h: commodity avg `0.0493` n `12`; crypto_alt avg `-2.1487` n `232`; crypto_major avg `-2.291` n `8`; equity avg `-0.9171` n `133`; fx avg `-0.0586` n `6`; index avg `-0.1287` n `26`; metal avg `-0.4362` n `20`; unknown avg `1.8089` n `785`
- 4h: commodity avg `0.0451` n `12`; crypto_alt avg `-1.3022` n `232`; crypto_major avg `-1.8016` n `8`; equity avg `-0.7707` n `133`; fx avg `-0.0671` n `6`; index avg `-0.0813` n `26`; metal avg `-0.5719` n `20`; unknown avg `1.0974` n `785`
- 24h: commodity avg `-0.4418` n `12`; crypto_alt avg `0.2673` n `232`; crypto_major avg `1.2527` n `8`; equity avg `1.0956` n `133`; fx avg `-0.0131` n `6`; index avg `0.2399` n `26`; metal avg `-0.2272` n `20`; unknown avg `1.4146` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
