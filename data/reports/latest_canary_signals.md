# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T09:37:34.491723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.43` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0923` n `12`; crypto_alt avg `-0.3432` n `228`; crypto_major avg `-0.3335` n `8`; equity avg `-0.0824` n `74`; fx avg `-0.0016` n `6`; index avg `-0.0225` n `23`; metal avg `-0.0494` n `18`; unknown avg `-0.0562` n `689`
- 1h: commodity avg `-0.085` n `12`; crypto_alt avg `-0.3076` n `228`; crypto_major avg `-0.3324` n `8`; equity avg `-0.2353` n `74`; fx avg `0.0171` n `6`; index avg `-0.0876` n `23`; metal avg `0.029` n `18`; unknown avg `0.1405` n `689`
- 4h: commodity avg `-0.4687` n `12`; crypto_alt avg `-0.3673` n `228`; crypto_major avg `-0.0838` n `8`; equity avg `0.0714` n `74`; fx avg `0.0208` n `6`; index avg `0.1994` n `23`; metal avg `0.3804` n `18`; unknown avg `0.8242` n `529`
- 24h: commodity avg `-1.188` n `12`; crypto_alt avg `2.6318` n `228`; crypto_major avg `2.8037` n `8`; equity avg `1.6098` n `74`; fx avg `0.0687` n `6`; index avg `0.9425` n `23`; metal avg `2.3149` n `18`; unknown avg `1.6717` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
