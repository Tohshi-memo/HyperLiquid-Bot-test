# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T17:07:31.626126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8299` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6863` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9575` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `0.048` n `229`; crypto_major avg `0.0927` n `8`; equity avg `-0.0314` n `88`; fx avg `0.0053` n `6`; index avg `-0.0077` n `25`; metal avg `0.0678` n `20`; unknown avg `0.0115` n `766`
- 1h: commodity avg `-0.1586` n `12`; crypto_alt avg `0.3741` n `229`; crypto_major avg `0.4776` n `8`; equity avg `-0.0525` n `88`; fx avg `0.0183` n `6`; index avg `-0.0235` n `25`; metal avg `0.1393` n `20`; unknown avg `0.1921` n `766`
- 4h: commodity avg `0.0701` n `12`; crypto_alt avg `3.0864` n `229`; crypto_major avg `2.9` n `8`; equity avg `0.9425` n `88`; fx avg `0.042` n `6`; index avg `0.1072` n `25`; metal avg `0.2137` n `20`; unknown avg `2.6124` n `765`
- 24h: commodity avg `-0.1709` n `12`; crypto_alt avg `1.3259` n `229`; crypto_major avg `1.0375` n `8`; equity avg `-0.0691` n `88`; fx avg `0.2153` n `6`; index avg `0.0658` n `25`; metal avg `-0.2329` n `20`; unknown avg `0.8362` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
