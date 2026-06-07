# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T11:07:21.678962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.0163` n `228`; crypto_major avg `-0.044` n `8`; equity avg `0.0333` n `74`; fx avg `0.0155` n `6`; index avg `-0.0024` n `23`; metal avg `-0.0029` n `18`; unknown avg `0.0445` n `516`
- 1h: commodity avg `0.0573` n `12`; crypto_alt avg `-0.2262` n `228`; crypto_major avg `-0.1056` n `8`; equity avg `-0.0181` n `74`; fx avg `0.0061` n `6`; index avg `0.0952` n `23`; metal avg `-0.0335` n `18`; unknown avg `-0.0111` n `516`
- 4h: commodity avg `-0.0959` n `12`; crypto_alt avg `-0.3739` n `228`; crypto_major avg `-0.0444` n `8`; equity avg `-0.2536` n `74`; fx avg `-0.0218` n `6`; index avg `-0.2013` n `23`; metal avg `-0.0189` n `18`; unknown avg `-4.8285` n `516`
- 24h: commodity avg `0.0144` n `12`; crypto_alt avg `2.7201` n `228`; crypto_major avg `2.7913` n `8`; equity avg `1.9658` n `74`; fx avg `0.0231` n `6`; index avg `0.6821` n `23`; metal avg `0.6105` n `18`; unknown avg `0.416` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
