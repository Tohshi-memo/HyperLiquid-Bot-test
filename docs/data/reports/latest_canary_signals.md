# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T07:22:32.285756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.83` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1572` n `12`; crypto_alt avg `0.2321` n `228`; crypto_major avg `0.1354` n `8`; equity avg `0.0926` n `74`; fx avg `0.0048` n `6`; index avg `0.0001` n `23`; metal avg `0.1639` n `16`; unknown avg `0.1011` n `674`
- 1h: commodity avg `-0.3037` n `12`; crypto_alt avg `0.0693` n `228`; crypto_major avg `0.1259` n `8`; equity avg `0.1626` n `74`; fx avg `-0.0019` n `6`; index avg `0.0951` n `23`; metal avg `0.1243` n `18`; unknown avg `0.4348` n `689`
- 4h: commodity avg `-0.136` n `12`; crypto_alt avg `0.3812` n `228`; crypto_major avg `0.2141` n `8`; equity avg `0.0606` n `74`; fx avg `0.0317` n `6`; index avg `0.2028` n `23`; metal avg `-0.223` n `18`; unknown avg `0.0025` n `529`
- 24h: commodity avg `-1.1098` n `12`; crypto_alt avg `3.1686` n `228`; crypto_major avg `3.007` n `8`; equity avg `1.9024` n `74`; fx avg `0.0385` n `6`; index avg `0.9936` n `23`; metal avg `1.8473` n `18`; unknown avg `1.7653` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
