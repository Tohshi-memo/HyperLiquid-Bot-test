# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T00:07:18.749720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0049` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.5418` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4183` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0439` n `12`; crypto_alt avg `-0.071` n `228`; crypto_major avg `0.0078` n `8`; equity avg `-0.0858` n `67`; fx avg `0.0214` n `6`; index avg `-0.0943` n `23`; metal avg `0.0869` n `18`; unknown avg `0.0343` n `419`
- 1h: commodity avg `0.2582` n `12`; crypto_alt avg `-0.0706` n `228`; crypto_major avg `-0.1229` n `8`; equity avg `-0.405` n `67`; fx avg `0.0148` n `6`; index avg `-0.2397` n `23`; metal avg `-0.1174` n `18`; unknown avg `1.4319` n `419`
- 4h: commodity avg `0.3809` n `12`; crypto_alt avg `-1.9903` n `228`; crypto_major avg `-1.624` n `8`; equity avg `-0.5096` n `67`; fx avg `0.0019` n `6`; index avg `-0.2057` n `23`; metal avg `-0.0822` n `18`; unknown avg `0.5935` n `419`
- 24h: commodity avg `-0.8495` n `12`; crypto_alt avg `-2.2538` n `228`; crypto_major avg `-1.6982` n `8`; equity avg `-0.8628` n `67`; fx avg `-0.0849` n `6`; index avg `-0.9117` n `23`; metal avg `-1.7292` n `18`; unknown avg `-0.673` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
