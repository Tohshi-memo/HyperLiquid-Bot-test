# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T17:22:28.297720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.06` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.7361` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.3738` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.353` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5792` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1747` n `12`; crypto_alt avg `0.2609` n `228`; crypto_major avg `0.2046` n `8`; equity avg `0.0472` n `69`; fx avg `0.0031` n `6`; index avg `-0.0055` n `23`; metal avg `-0.0721` n `18`; unknown avg `0.0095` n `422`
- 1h: commodity avg `0.2449` n `12`; crypto_alt avg `0.3747` n `228`; crypto_major avg `0.0063` n `8`; equity avg `-0.0291` n `69`; fx avg `-0.022` n `6`; index avg `-0.0421` n `23`; metal avg `-0.2305` n `18`; unknown avg `-0.4252` n `422`
- 4h: commodity avg `0.8006` n `12`; crypto_alt avg `-2.0405` n `228`; crypto_major avg `-1.9355` n `8`; equity avg `0.4383` n `69`; fx avg `-0.0331` n `6`; index avg `0.4175` n `23`; metal avg `-0.3563` n `18`; unknown avg `-0.049` n `422`
- 24h: commodity avg `-0.0822` n `12`; crypto_alt avg `-2.2954` n `228`; crypto_major avg `-3.089` n `8`; equity avg `0.403` n `69`; fx avg `0.1041` n `6`; index avg `0.4036` n `23`; metal avg `0.5167` n `18`; unknown avg `0.0355` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
