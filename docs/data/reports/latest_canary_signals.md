# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T00:37:25.355184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3808` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.525` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `0.8674` n `228`; crypto_major avg `0.933` n `8`; equity avg `0.5386` n `74`; fx avg `-0.0122` n `6`; index avg `0.2651` n `23`; metal avg `0.0583` n `18`; unknown avg `-0.0857` n `517`
- 1h: commodity avg `-0.0383` n `12`; crypto_alt avg `0.8063` n `228`; crypto_major avg `1.1164` n `8`; equity avg `1.431` n `74`; fx avg `-0.0132` n `6`; index avg `0.6307` n `23`; metal avg `0.3524` n `18`; unknown avg `0.019` n `517`
- 4h: commodity avg `-0.1988` n `12`; crypto_alt avg `2.597` n `228`; crypto_major avg `3.182` n `8`; equity avg `1.845` n `74`; fx avg `-0.0478` n `6`; index avg `0.6933` n `23`; metal avg `0.657` n `18`; unknown avg `0.7325` n `516`
- 24h: commodity avg `-0.0076` n `12`; crypto_alt avg `3.3056` n `228`; crypto_major avg `5.6037` n `8`; equity avg `2.6426` n `74`; fx avg `-0.0602` n `6`; index avg `0.9487` n `23`; metal avg `0.9053` n `18`; unknown avg `-4.4334` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
