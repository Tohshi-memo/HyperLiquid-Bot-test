# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T15:07:20.457463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0118` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1532` n `12`; crypto_alt avg `-0.0537` n `228`; crypto_major avg `-0.0777` n `8`; equity avg `0.0079` n `67`; fx avg `-0.0043` n `6`; index avg `-0.0472` n `23`; metal avg `-0.0693` n `18`; unknown avg `-0.0827` n `396`
- 1h: commodity avg `0.7756` n `12`; crypto_alt avg `-0.3171` n `228`; crypto_major avg `-0.5264` n `8`; equity avg `-0.2389` n `67`; fx avg `-0.0115` n `6`; index avg `-0.2147` n `23`; metal avg `-0.3983` n `18`; unknown avg `0.755` n `396`
- 4h: commodity avg `1.0369` n `12`; crypto_alt avg `-1.2633` n `228`; crypto_major avg `-0.9749` n `8`; equity avg `-0.3267` n `67`; fx avg `0.0113` n `6`; index avg `-0.3544` n `23`; metal avg `-0.6213` n `18`; unknown avg `1.4953` n `396`
- 24h: commodity avg `-0.973` n `12`; crypto_alt avg `0.431` n `228`; crypto_major avg `2.042` n `8`; equity avg `1.6397` n `67`; fx avg `0.0824` n `6`; index avg `0.4737` n `23`; metal avg `0.5131` n `18`; unknown avg `2.019` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
