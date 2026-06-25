# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T16:22:35.465141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.3534` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.1297` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6174` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.1399` n `228`; crypto_major avg `0.2709` n `8`; equity avg `0.2354` n `86`; fx avg `0.0119` n `6`; index avg `0.0514` n `23`; metal avg `0.0589` n `20`; unknown avg `0.2116` n `765`
- 1h: commodity avg `0.0444` n `12`; crypto_alt avg `0.9098` n `228`; crypto_major avg `1.0869` n `8`; equity avg `0.5071` n `86`; fx avg `0.0257` n `6`; index avg `0.1116` n `23`; metal avg `0.0895` n `20`; unknown avg `0.3101` n `765`
- 4h: commodity avg `0.3534` n `12`; crypto_alt avg `-1.2756` n `228`; crypto_major avg `-1.7763` n `8`; equity avg `-1.9927` n `86`; fx avg `0.0975` n `6`; index avg `-0.1589` n `23`; metal avg `0.5771` n `20`; unknown avg `0.8925` n `765`
- 24h: commodity avg `0.354` n `12`; crypto_alt avg `-1.2577` n `228`; crypto_major avg `-1.1483` n `8`; equity avg `-0.6075` n `86`; fx avg `0.0954` n `6`; index avg `0.3353` n `23`; metal avg `0.3987` n `20`; unknown avg `-0.0167` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
