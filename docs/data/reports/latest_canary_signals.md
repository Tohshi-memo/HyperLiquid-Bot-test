# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T13:52:24.811406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `0.0603` n `230`; crypto_major avg `0.0139` n `8`; equity avg `0.2899` n `113`; fx avg `-0.0122` n `6`; index avg `0.0792` n `25`; metal avg `0.0393` n `20`; unknown avg `0.0165` n `787`
- 1h: commodity avg `-0.1177` n `12`; crypto_alt avg `0.1538` n `230`; crypto_major avg `0.2184` n `8`; equity avg `1.2426` n `113`; fx avg `-0.0128` n `6`; index avg `0.1709` n `25`; metal avg `-0.1033` n `20`; unknown avg `0.0318` n `787`
- 4h: commodity avg `-0.1807` n `12`; crypto_alt avg `0.0002` n `230`; crypto_major avg `-0.032` n `8`; equity avg `1.3601` n `113`; fx avg `-0.0357` n `6`; index avg `0.2048` n `25`; metal avg `0.0036` n `20`; unknown avg `0.0872` n `787`
- 24h: commodity avg `-0.4394` n `12`; crypto_alt avg `-0.5898` n `230`; crypto_major avg `0.099` n `8`; equity avg `1.6073` n `113`; fx avg `0.0027` n `6`; index avg `0.2045` n `25`; metal avg `-0.5761` n `20`; unknown avg `0.3181` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2302`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1998`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
