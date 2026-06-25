# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T10:07:33.518441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0373` n `12`; crypto_alt avg `-0.0169` n `228`; crypto_major avg `-0.0321` n `8`; equity avg `0.0579` n `86`; fx avg `-0.0168` n `6`; index avg `-0.0048` n `23`; metal avg `-0.0735` n `20`; unknown avg `-0.0093` n `765`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `-0.1669` n `228`; crypto_major avg `-0.1467` n `8`; equity avg `0.0681` n `86`; fx avg `-0.0025` n `6`; index avg `-0.0107` n `23`; metal avg `-0.048` n `20`; unknown avg `-0.1445` n `765`
- 4h: commodity avg `0.1684` n `12`; crypto_alt avg `-0.3288` n `228`; crypto_major avg `-0.1631` n `8`; equity avg `0.1198` n `86`; fx avg `0.0049` n `6`; index avg `-0.0294` n `23`; metal avg `0.1979` n `20`; unknown avg `0.0531` n `749`
- 24h: commodity avg `-0.3008` n `12`; crypto_alt avg `-1.2178` n `228`; crypto_major avg `-0.8129` n `8`; equity avg `0.1659` n `86`; fx avg `-0.0266` n `6`; index avg `0.5048` n `23`; metal avg `-1.2157` n `20`; unknown avg `-0.5335` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
