# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T20:37:27.471387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `0.1303` n `228`; crypto_major avg `0.1201` n `8`; equity avg `0.0182` n `69`; fx avg `0.0047` n `6`; index avg `-0.0225` n `23`; metal avg `-0.0114` n `18`; unknown avg `-0.0069` n `417`
- 1h: commodity avg `0.2461` n `12`; crypto_alt avg `0.1483` n `228`; crypto_major avg `0.1354` n `8`; equity avg `0.0209` n `69`; fx avg `0.013` n `6`; index avg `-0.1936` n `23`; metal avg `-0.0507` n `18`; unknown avg `0.1529` n `417`
- 4h: commodity avg `0.1356` n `12`; crypto_alt avg `1.169` n `228`; crypto_major avg `0.9654` n `8`; equity avg `0.6896` n `69`; fx avg `0.0011` n `6`; index avg `-0.1476` n `23`; metal avg `-0.0078` n `18`; unknown avg `0.5451` n `417`
- 24h: commodity avg `1.034` n `12`; crypto_alt avg `-3.3101` n `228`; crypto_major avg `-1.0714` n `8`; equity avg `1.5539` n `69`; fx avg `-0.0211` n `6`; index avg `0.6824` n `23`; metal avg `0.5427` n `18`; unknown avg `-0.6512` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
