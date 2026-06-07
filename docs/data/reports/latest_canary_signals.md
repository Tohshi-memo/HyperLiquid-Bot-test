# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T23:22:21.831091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8659` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2224` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9201` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1631` n `12`; crypto_alt avg `-0.078` n `228`; crypto_major avg `-0.0135` n `8`; equity avg `-0.1071` n `74`; fx avg `0.0009` n `6`; index avg `-0.0047` n `23`; metal avg `0.1016` n `18`; unknown avg `-0.0377` n `516`
- 1h: commodity avg `-0.148` n `12`; crypto_alt avg `-0.7689` n `228`; crypto_major avg `-0.2913` n `8`; equity avg `-0.1655` n `74`; fx avg `-0.0077` n `6`; index avg `-0.1256` n `23`; metal avg `0.0836` n `18`; unknown avg `-0.0377` n `516`
- 4h: commodity avg `-0.6527` n `12`; crypto_alt avg `2.0081` n `228`; crypto_major avg `2.2132` n `8`; equity avg `0.2931` n `74`; fx avg `-0.0456` n `6`; index avg `-0.0444` n `23`; metal avg `-0.0092` n `18`; unknown avg `0.6564` n `516`
- 24h: commodity avg `0.1243` n `12`; crypto_alt avg `3.103` n `228`; crypto_major avg `4.7785` n `8`; equity avg `1.3095` n `74`; fx avg `-0.0587` n `6`; index avg `0.1429` n `23`; metal avg `0.445` n `18`; unknown avg `-4.5599` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
