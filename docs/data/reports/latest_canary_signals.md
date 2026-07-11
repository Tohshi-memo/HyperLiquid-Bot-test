# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T19:52:29.563086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `12`; crypto_alt avg `-0.0139` n `230`; crypto_major avg `-0.0189` n `8`; equity avg `0.0009` n `92`; fx avg `0.0016` n `6`; index avg `0.003` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0257` n `765`
- 1h: commodity avg `-0.0394` n `12`; crypto_alt avg `-0.0075` n `230`; crypto_major avg `-0.0455` n `8`; equity avg `0.0158` n `92`; fx avg `-0.0006` n `6`; index avg `0.0138` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.1404` n `765`
- 4h: commodity avg `0.0187` n `12`; crypto_alt avg `0.3387` n `230`; crypto_major avg `0.2385` n `8`; equity avg `0.2513` n `92`; fx avg `0.0073` n `6`; index avg `0.0118` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.0566` n `765`
- 24h: commodity avg `-0.0226` n `12`; crypto_alt avg `1.0334` n `229`; crypto_major avg `0.6618` n `8`; equity avg `0.3336` n `92`; fx avg `-0.0012` n `6`; index avg `0.0414` n `25`; metal avg `0.0499` n `20`; unknown avg `2.3407` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
