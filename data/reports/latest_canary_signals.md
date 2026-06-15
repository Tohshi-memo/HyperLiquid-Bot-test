# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T14:37:39.660311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.19` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.6172` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0795` n `12`; crypto_alt avg `0.1035` n `228`; crypto_major avg `-0.1263` n `8`; equity avg `0.1573` n `74`; fx avg `-0.0087` n `6`; index avg `0.0103` n `23`; metal avg `0.0745` n `18`; unknown avg `0.1604` n `690`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `-0.2446` n `228`; crypto_major avg `-0.4847` n `8`; equity avg `-0.0296` n `74`; fx avg `-0.0181` n `6`; index avg `-0.0952` n `23`; metal avg `-0.191` n `18`; unknown avg `0.4703` n `690`
- 4h: commodity avg `0.3099` n `12`; crypto_alt avg `1.9139` n `228`; crypto_major avg `1.9641` n `8`; equity avg `0.5108` n `74`; fx avg `-0.0243` n `6`; index avg `0.2032` n `23`; metal avg `0.3469` n `18`; unknown avg `0.6077` n `689`
- 24h: commodity avg `-1.2471` n `12`; crypto_alt avg `6.619` n `228`; crypto_major avg `6.4406` n `8`; equity avg `2.4693` n `74`; fx avg `0.035` n `6`; index avg `1.0692` n `23`; metal avg `2.9107` n `18`; unknown avg `2.378` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
