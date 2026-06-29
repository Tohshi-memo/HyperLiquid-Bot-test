# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T02:22:29.631504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.1442` n `228`; crypto_major avg `-0.0219` n `8`; equity avg `-0.0484` n `88`; fx avg `0.0022` n `6`; index avg `-0.0049` n `23`; metal avg `0.093` n `20`; unknown avg `1.1056` n `764`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `0.0226` n `228`; crypto_major avg `0.0051` n `8`; equity avg `-0.0253` n `88`; fx avg `0.0495` n `6`; index avg `-0.0089` n `23`; metal avg `0.1243` n `20`; unknown avg `0.7315` n `764`
- 4h: commodity avg `-0.0169` n `12`; crypto_alt avg `0.177` n `228`; crypto_major avg `0.1519` n `8`; equity avg `-0.6196` n `88`; fx avg `0.0964` n `6`; index avg `-0.2259` n `23`; metal avg `0.0494` n `20`; unknown avg `1.3951` n `762`
- 24h: commodity avg `-0.4924` n `12`; crypto_alt avg `-0.4351` n `228`; crypto_major avg `-0.6158` n `8`; equity avg `-0.2286` n `88`; fx avg `0.019` n `6`; index avg `-0.0849` n `23`; metal avg `-0.1578` n `20`; unknown avg `15.0998` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
