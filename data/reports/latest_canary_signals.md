# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T20:37:29.561953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `0.1772` n `230`; crypto_major avg `0.2117` n `8`; equity avg `0.0198` n `113`; fx avg `-0.0002` n `6`; index avg `-0.0057` n `25`; metal avg `0.0099` n `20`; unknown avg `0.1596` n `786`
- 1h: commodity avg `-0.0431` n `12`; crypto_alt avg `0.2331` n `230`; crypto_major avg `0.1711` n `8`; equity avg `-0.2376` n `113`; fx avg `0.002` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0177` n `20`; unknown avg `0.1517` n `786`
- 4h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.077` n `230`; crypto_major avg `-0.0224` n `8`; equity avg `-0.1032` n `113`; fx avg `0.0006` n `6`; index avg `0.0174` n `25`; metal avg `-0.0784` n `20`; unknown avg `0.4747` n `786`
- 24h: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.6699` n `230`; crypto_major avg `0.1154` n `8`; equity avg `2.8377` n `113`; fx avg `0.0303` n `6`; index avg `0.3656` n `25`; metal avg `0.173` n `20`; unknown avg `0.0753` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
