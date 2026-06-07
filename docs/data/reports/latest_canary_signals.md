# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T20:52:25.129877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0351` n `12`; crypto_alt avg `0.2494` n `228`; crypto_major avg `0.1766` n `8`; equity avg `0.0418` n `74`; fx avg `-0.0323` n `6`; index avg `-0.0211` n `23`; metal avg `-0.0218` n `18`; unknown avg `-0.0001` n `516`
- 1h: commodity avg `-0.4202` n `12`; crypto_alt avg `1.0818` n `228`; crypto_major avg `1.0336` n `8`; equity avg `0.2554` n `74`; fx avg `-0.0415` n `6`; index avg `0.1505` n `23`; metal avg `-0.0226` n `18`; unknown avg `0.5723` n `516`
- 4h: commodity avg `0.1257` n `12`; crypto_alt avg `-1.0373` n `228`; crypto_major avg `-0.372` n `8`; equity avg `-0.7342` n `74`; fx avg `-0.0219` n `6`; index avg `-0.2638` n `23`; metal avg `-0.3099` n `18`; unknown avg `-2.4541` n `516`
- 24h: commodity avg `0.2346` n `12`; crypto_alt avg `2.2764` n `228`; crypto_major avg `3.4294` n `8`; equity avg `1.1141` n `74`; fx avg `-0.0886` n `6`; index avg `0.1753` n `23`; metal avg `0.3111` n `18`; unknown avg `-4.5365` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
