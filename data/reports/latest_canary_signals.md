# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T20:37:24.466231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `2.8143` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.5164` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.2559` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.9666` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0368` n `12`; crypto_alt avg `0.5146` n `228`; crypto_major avg `0.4426` n `8`; equity avg `-0.057` n `74`; fx avg `0.0103` n `6`; index avg `-0.041` n `23`; metal avg `0.1395` n `18`; unknown avg `-0.1561` n `425`
- 1h: commodity avg `0.0397` n `12`; crypto_alt avg `2.5706` n `228`; crypto_major avg `2.2956` n `8`; equity avg `-0.5187` n `74`; fx avg `0.004` n `6`; index avg `-0.4789` n `23`; metal avg `-0.2208` n `18`; unknown avg `1.2734` n `425`
- 4h: commodity avg `0.1293` n `12`; crypto_alt avg `0.7147` n `228`; crypto_major avg `0.5675` n `8`; equity avg `-1.3991` n `74`; fx avg `-0.0446` n `6`; index avg `-1.6054` n `23`; metal avg `-0.6259` n `18`; unknown avg `-0.172` n `424`
- 24h: commodity avg `-1.625` n `12`; crypto_alt avg `-7.5373` n `228`; crypto_major avg `-6.1737` n `8`; equity avg `-6.6147` n `74`; fx avg `-0.0455` n `6`; index avg `-4.5775` n `23`; metal avg `-4.6399` n `18`; unknown avg `-2.2554` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
