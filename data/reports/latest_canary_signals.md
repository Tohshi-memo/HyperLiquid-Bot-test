# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T00:22:25.815591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3322` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5828` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.053` n `12`; crypto_alt avg `-0.0584` n `228`; crypto_major avg `0.129` n `8`; equity avg `0.5751` n `74`; fx avg `0.0119` n `6`; index avg `0.2715` n `23`; metal avg `0.1712` n `18`; unknown avg `-0.0492` n `517`
- 1h: commodity avg `-0.0329` n `12`; crypto_alt avg `0.185` n `228`; crypto_major avg `0.578` n `8`; equity avg `1.0036` n `74`; fx avg `0.0053` n `6`; index avg `0.4964` n `23`; metal avg `0.5028` n `18`; unknown avg `0.0543` n `516`
- 4h: commodity avg `-0.1712` n `12`; crypto_alt avg `1.6082` n `228`; crypto_major avg `2.161` n `8`; equity avg `1.3074` n `74`; fx avg `-0.0371` n `6`; index avg `0.4409` n `23`; metal avg `0.5782` n `18`; unknown avg `0.6453` n `516`
- 24h: commodity avg `0.0389` n `12`; crypto_alt avg `2.7502` n `228`; crypto_major avg `5.0212` n `8`; equity avg `2.114` n `74`; fx avg `-0.052` n `6`; index avg `0.624` n `23`; metal avg `0.8449` n `18`; unknown avg `-4.762` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
