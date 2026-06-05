# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T06:37:24.593765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.6684` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.5786` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.5545` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.8596` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-2.6604` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.6069` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.4908` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `-1.8815` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0608` n `12`; crypto_alt avg `0.049` n `228`; crypto_major avg `0.3036` n `8`; equity avg `-0.0366` n `74`; fx avg `-0.0441` n `6`; index avg `0.0619` n `23`; metal avg `0.4279` n `18`; unknown avg `0.7333` n `424`
- 1h: commodity avg `-0.1806` n `12`; crypto_alt avg `-3.6542` n `228`; crypto_major avg `-2.6714` n `8`; equity avg `-0.7899` n `74`; fx avg `-0.0072` n `6`; index avg `-0.0645` n `23`; metal avg `-0.011` n `18`; unknown avg `-1.2075` n `404`
- 4h: commodity avg `-0.1689` n `12`; crypto_alt avg `-4.4606` n `228`; crypto_major avg `-3.7475` n `8`; equity avg `-0.8879` n `74`; fx avg `-0.0443` n `6`; index avg `-0.193` n `23`; metal avg `-0.0791` n `18`; unknown avg `-1.6439` n `404`
- 24h: commodity avg `-0.1331` n `12`; crypto_alt avg `-8.5495` n `228`; crypto_major avg `-7.0086` n `8`; equity avg `-2.0837` n `73`; fx avg `0.1324` n `6`; index avg `-0.5554` n `23`; metal avg `-0.4875` n `18`; unknown avg `-1.6707` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
