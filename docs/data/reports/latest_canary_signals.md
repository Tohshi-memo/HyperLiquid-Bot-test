# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T05:07:15.496786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.0389` n `228`; crypto_major avg `-0.1569` n `8`; equity avg `-0.01` n `65`; fx avg `-0.0006` n `5`; index avg `-0.0084` n `23`; metal avg `0.0011` n `18`; unknown avg `0.0232` n `375`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `-0.1958` n `228`; crypto_major avg `-0.5229` n `8`; equity avg `-0.0424` n `65`; fx avg `-0.0013` n `5`; index avg `-0.0157` n `23`; metal avg `-0.0369` n `18`; unknown avg `-0.3738` n `375`
- 4h: commodity avg `0.2658` n `12`; crypto_alt avg `0.3444` n `228`; crypto_major avg `0.325` n `8`; equity avg `0.0322` n `65`; fx avg `0.0004` n `5`; index avg `0.1475` n `23`; metal avg `0.0767` n `18`; unknown avg `-0.1031` n `375`
- 24h: commodity avg `-0.1993` n `12`; crypto_alt avg `4.2744` n `228`; crypto_major avg `2.6518` n `8`; equity avg `3.5781` n `65`; fx avg `0.0393` n `5`; index avg `1.3884` n `23`; metal avg `0.235` n `18`; unknown avg `1.4227` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
