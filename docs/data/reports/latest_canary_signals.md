# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T21:06:20.944913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.5765` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `3.0087` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5717` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.5627` n `12`; crypto_alt avg `0.2259` n `228`; crypto_major avg `0.2178` n `8`; equity avg `0.157` n `67`; fx avg `0.0018` n `6`; index avg `-0.0075` n `23`; metal avg `0.2022` n `18`; unknown avg `1.1839` n `396`
- 1h: commodity avg `-1.373` n `12`; crypto_alt avg `1.7224` n `228`; crypto_major avg `1.6357` n `8`; equity avg `0.5783` n `67`; fx avg `0.0396` n `6`; index avg `0.1241` n `23`; metal avg `0.6536` n `18`; unknown avg `1.1762` n `396`
- 4h: commodity avg `-2.2132` n `12`; crypto_alt avg `2.6133` n `228`; crypto_major avg `2.3633` n `8`; equity avg `1.2234` n `67`; fx avg `0.0349` n `6`; index avg `0.5489` n `23`; metal avg `0.7916` n `18`; unknown avg `3.8606` n `396`
- 24h: commodity avg `-2.3119` n `12`; crypto_alt avg `2.2761` n `228`; crypto_major avg `2.1911` n `8`; equity avg `1.2064` n `67`; fx avg `0.0109` n `6`; index avg `0.5831` n `23`; metal avg `0.8719` n `18`; unknown avg `-0.3333` n `376`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
