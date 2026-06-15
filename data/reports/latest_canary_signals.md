# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T10:22:32.710256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1757` n `12`; crypto_alt avg `0.069` n `228`; crypto_major avg `0.099` n `8`; equity avg `-0.0309` n `74`; fx avg `0.01` n `6`; index avg `0.0159` n `23`; metal avg `-0.0048` n `18`; unknown avg `0.0911` n `689`
- 1h: commodity avg `0.0846` n `12`; crypto_alt avg `0.049` n `228`; crypto_major avg `0.2047` n `8`; equity avg `-0.0896` n `74`; fx avg `0.0133` n `6`; index avg `0.0183` n `23`; metal avg `-0.1184` n `18`; unknown avg `0.0255` n `689`
- 4h: commodity avg `-0.2293` n `12`; crypto_alt avg `0.0889` n `228`; crypto_major avg `0.3879` n `8`; equity avg `0.0471` n `74`; fx avg `0.0171` n `6`; index avg `0.1206` n `23`; metal avg `0.5494` n `18`; unknown avg `1.2891` n `689`
- 24h: commodity avg `-0.9461` n `12`; crypto_alt avg `2.8149` n `228`; crypto_major avg `2.9665` n `8`; equity avg `1.4168` n `74`; fx avg `0.0623` n `6`; index avg `0.9107` n `23`; metal avg `2.2417` n `18`; unknown avg `1.5523` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
