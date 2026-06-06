# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T16:07:22.305255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.2359` n `228`; crypto_major avg `0.0135` n `8`; equity avg `-0.0123` n `74`; fx avg `0.0` n `6`; index avg `0.0288` n `23`; metal avg `0.0442` n `18`; unknown avg `-1.9275` n `515`
- 1h: commodity avg `-0.0266` n `12`; crypto_alt avg `0.3636` n `228`; crypto_major avg `0.415` n `8`; equity avg `-0.022` n `74`; fx avg `0.0189` n `6`; index avg `0.0821` n `23`; metal avg `0.0666` n `18`; unknown avg `-3.8881` n `515`
- 4h: commodity avg `0.0853` n `12`; crypto_alt avg `0.1843` n `228`; crypto_major avg `-0.2546` n `8`; equity avg `0.2454` n `74`; fx avg `0.0199` n `6`; index avg `0.3625` n `23`; metal avg `-0.1782` n `18`; unknown avg `-0.439` n `415`
- 24h: commodity avg `0.01` n `12`; crypto_alt avg `-0.0053` n `228`; crypto_major avg `-0.1458` n `8`; equity avg `-2.5862` n `74`; fx avg `-0.0483` n `6`; index avg `-1.6797` n `23`; metal avg `-1.1678` n `18`; unknown avg `-0.1766` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
