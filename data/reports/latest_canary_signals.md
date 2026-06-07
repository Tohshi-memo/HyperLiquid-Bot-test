# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T23:07:24.846205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2152` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9401` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5987` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0434` n `12`; crypto_alt avg `-0.5037` n `228`; crypto_major avg `-0.4361` n `8`; equity avg `-0.1857` n `74`; fx avg `-0.0016` n `6`; index avg `-0.0373` n `23`; metal avg `-0.0618` n `18`; unknown avg `-0.025` n `516`
- 1h: commodity avg `-0.1803` n `12`; crypto_alt avg `1.3242` n `228`; crypto_major avg `1.5508` n `8`; equity avg `0.4417` n `74`; fx avg `0.0002` n `6`; index avg `0.1006` n `23`; metal avg `0.1455` n `18`; unknown avg `0.3609` n `516`
- 4h: commodity avg `-0.3746` n `12`; crypto_alt avg `1.7263` n `228`; crypto_major avg `1.8406` n `8`; equity avg `0.2419` n `74`; fx avg `-0.0339` n `6`; index avg `-0.0195` n `23`; metal avg `-0.0995` n `18`; unknown avg `0.808` n `516`
- 24h: commodity avg `0.2958` n `12`; crypto_alt avg `3.037` n `228`; crypto_major avg `4.6628` n `8`; equity avg `1.4651` n `74`; fx avg `-0.0615` n `6`; index avg `0.1569` n `23`; metal avg `0.3092` n `18`; unknown avg `-4.5913` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
