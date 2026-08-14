# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T06:52:24.843830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.1369` n `230`; crypto_major avg `-0.1049` n `8`; equity avg `0.0745` n `113`; fx avg `-0.0004` n `6`; index avg `0.0099` n `25`; metal avg `0.0221` n `20`; unknown avg `0.0644` n `787`
- 1h: commodity avg `0.0781` n `12`; crypto_alt avg `-0.2209` n `230`; crypto_major avg `-0.3693` n `8`; equity avg `-0.02` n `113`; fx avg `0.0587` n `6`; index avg `-0.005` n `25`; metal avg `0.0379` n `20`; unknown avg `-0.0179` n `755`
- 4h: commodity avg `0.1804` n `12`; crypto_alt avg `-0.5237` n `230`; crypto_major avg `-0.6846` n `8`; equity avg `-0.0809` n `113`; fx avg `0.0606` n `6`; index avg `0.0099` n `25`; metal avg `0.0908` n `20`; unknown avg `-0.0796` n `755`
- 24h: commodity avg `-0.2552` n `12`; crypto_alt avg `-0.6636` n `230`; crypto_major avg `-0.9263` n `8`; equity avg `1.08` n `113`; fx avg `-0.0316` n `6`; index avg `0.2654` n `25`; metal avg `-0.2982` n `20`; unknown avg `0.9998` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2263`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1906`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
