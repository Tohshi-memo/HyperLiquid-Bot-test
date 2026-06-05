# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T13:37:24.147042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `2.2428` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.7175` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.15` n `12`; crypto_alt avg `0.1508` n `228`; crypto_major avg `-0.0092` n `8`; equity avg `-0.6193` n `74`; fx avg `-0.0032` n `6`; index avg `-0.4991` n `23`; metal avg `-0.631` n `18`; unknown avg `0.1061` n `424`
- 1h: commodity avg `-0.5041` n `12`; crypto_alt avg `1.2686` n `228`; crypto_major avg `0.9251` n `8`; equity avg `-0.7924` n `74`; fx avg `0.0074` n `6`; index avg `-0.6025` n `23`; metal avg `-1.3177` n `18`; unknown avg `0.3264` n `424`
- 4h: commodity avg `-0.5502` n `12`; crypto_alt avg `-0.1081` n `228`; crypto_major avg `-0.043` n `8`; equity avg `-1.3427` n `74`; fx avg `0.0128` n `6`; index avg `-0.8932` n `23`; metal avg `-1.3582` n `18`; unknown avg `1.8817` n `424`
- 24h: commodity avg `-0.7041` n `12`; crypto_alt avg `-5.4863` n `228`; crypto_major avg `-3.8872` n `8`; equity avg `-2.5209` n `74`; fx avg `0.1017` n `6`; index avg `-1.0869` n `23`; metal avg `-2.7265` n `18`; unknown avg `0.3432` n `404`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
