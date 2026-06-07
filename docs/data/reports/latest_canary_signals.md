# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T22:37:21.090079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.6795` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.3999` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.0324` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7026` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `0.123` n `228`; crypto_major avg `0.358` n `8`; equity avg `0.1628` n `74`; fx avg `-0.0008` n `6`; index avg `-0.0433` n `23`; metal avg `0.0396` n `18`; unknown avg `-0.0145` n `516`
- 1h: commodity avg `-0.2334` n `12`; crypto_alt avg `2.6552` n `228`; crypto_major avg `2.4461` n `8`; equity avg `0.4137` n `74`; fx avg `-0.0135` n `6`; index avg `-0.0852` n `23`; metal avg `0.0462` n `18`; unknown avg `0.3835` n `516`
- 4h: commodity avg `-0.0214` n `12`; crypto_alt avg `1.3592` n `228`; crypto_major avg `1.4934` n `8`; equity avg `0.1289` n `74`; fx avg `-0.0244` n `6`; index avg `-0.0381` n `23`; metal avg `-0.2092` n `18`; unknown avg `0.092` n `516`
- 24h: commodity avg `0.2876` n `12`; crypto_alt avg `4.1925` n `228`; crypto_major avg `5.7028` n `8`; equity avg `1.811` n `74`; fx avg `-0.0618` n `6`; index avg `0.2616` n `23`; metal avg `0.383` n `18`; unknown avg `-4.3355` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
