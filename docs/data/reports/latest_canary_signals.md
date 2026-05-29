# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T01:37:19.740929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0955` n `12`; crypto_alt avg `-0.0237` n `228`; crypto_major avg `-0.1295` n `8`; equity avg `-0.0229` n `69`; fx avg `-0.0015` n `6`; index avg `-0.0622` n `23`; metal avg `-0.2129` n `18`; unknown avg `-0.2395` n `417`
- 1h: commodity avg `0.1745` n `12`; crypto_alt avg `-0.3471` n `228`; crypto_major avg `-0.4891` n `8`; equity avg `-0.1675` n `69`; fx avg `0.016` n `6`; index avg `-0.0803` n `23`; metal avg `0.3554` n `18`; unknown avg `-0.2069` n `417`
- 4h: commodity avg `0.1443` n `12`; crypto_alt avg `-0.4268` n `228`; crypto_major avg `-0.6565` n `8`; equity avg `0.2273` n `69`; fx avg `0.0894` n `6`; index avg `-0.1144` n `23`; metal avg `0.3321` n `18`; unknown avg `-0.473` n `417`
- 24h: commodity avg `0.6023` n `12`; crypto_alt avg `-1.1363` n `228`; crypto_major avg `0.2072` n `8`; equity avg `2.5073` n `69`; fx avg `0.0445` n `6`; index avg `0.7757` n `23`; metal avg `1.5658` n `18`; unknown avg `-0.25` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
