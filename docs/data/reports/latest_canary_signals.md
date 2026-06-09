# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T08:07:27.285689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1111` n `12`; crypto_alt avg `-0.3531` n `228`; crypto_major avg `-0.3666` n `8`; equity avg `-0.0919` n `74`; fx avg `0.0149` n `6`; index avg `0.059` n `23`; metal avg `-0.1106` n `18`; unknown avg `0.0431` n `547`
- 1h: commodity avg `0.2456` n `12`; crypto_alt avg `-0.4641` n `228`; crypto_major avg `-0.6957` n `8`; equity avg `-0.3816` n `74`; fx avg `0.0519` n `6`; index avg `-0.0857` n `23`; metal avg `-0.0614` n `18`; unknown avg `0.0569` n `547`
- 4h: commodity avg `0.2117` n `12`; crypto_alt avg `1.1406` n `228`; crypto_major avg `0.578` n `8`; equity avg `0.2751` n `74`; fx avg `0.0569` n `6`; index avg `0.1827` n `23`; metal avg `0.2183` n `18`; unknown avg `0.4149` n `503`
- 24h: commodity avg `-1.0058` n `12`; crypto_alt avg `-0.1638` n `228`; crypto_major avg `0.2275` n `8`; equity avg `2.0726` n `74`; fx avg `-0.0165` n `6`; index avg `1.0367` n `23`; metal avg `0.7441` n `18`; unknown avg `-2.8869` n `503`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
