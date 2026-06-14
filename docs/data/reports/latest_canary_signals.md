# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T23:52:34.132658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.4815` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `4.18` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.2431` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6393` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.059` n `12`; crypto_alt avg `0.2274` n `228`; crypto_major avg `0.1928` n `8`; equity avg `0.1154` n `74`; fx avg `-0.0823` n `6`; index avg `-0.0092` n `23`; metal avg `0.2642` n `18`; unknown avg `-0.0492` n `645`
- 1h: commodity avg `-0.2452` n `12`; crypto_alt avg `0.4131` n `228`; crypto_major avg `0.5925` n `8`; equity avg `-0.0861` n `74`; fx avg `-0.0852` n `6`; index avg `-0.0609` n `23`; metal avg `0.1192` n `18`; unknown avg `-0.183` n `637`
- 4h: commodity avg `-1.0065` n `12`; crypto_alt avg `3.2623` n `228`; crypto_major avg `3.475` n `8`; equity avg `1.2319` n `74`; fx avg `0.0342` n `6`; index avg `0.1958` n `23`; metal avg `1.8357` n `18`; unknown avg `3.89` n `637`
- 24h: commodity avg `-0.6732` n `12`; crypto_alt avg `1.945` n `228`; crypto_major avg `2.4183` n `8`; equity avg `1.372` n `74`; fx avg `0.0225` n `6`; index avg `0.3502` n `23`; metal avg `1.7031` n `18`; unknown avg `1.497` n `585`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
