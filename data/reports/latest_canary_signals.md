# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T02:37:21.877724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.4553` n `228`; crypto_major avg `0.6154` n `8`; equity avg `0.2499` n `69`; fx avg `0.0047` n `6`; index avg `0.0347` n `23`; metal avg `-0.0302` n `18`; unknown avg `-0.1592` n `422`
- 1h: commodity avg `0.0242` n `12`; crypto_alt avg `0.1803` n `228`; crypto_major avg `0.5682` n `8`; equity avg `0.1526` n `69`; fx avg `0.0072` n `6`; index avg `-0.1322` n `23`; metal avg `-0.2654` n `18`; unknown avg `0.4077` n `422`
- 4h: commodity avg `-0.4937` n `12`; crypto_alt avg `-0.1324` n `228`; crypto_major avg `0.2764` n `8`; equity avg `-0.422` n `69`; fx avg `0.0508` n `6`; index avg `-0.4937` n `23`; metal avg `0.123` n `18`; unknown avg `0.5725` n `422`
- 24h: commodity avg `-0.4141` n `12`; crypto_alt avg `-1.0292` n `228`; crypto_major avg `-0.9809` n `8`; equity avg `-0.8544` n `69`; fx avg `0.0007` n `6`; index avg `0.2576` n `23`; metal avg `-0.4977` n `18`; unknown avg `2.1168` n `406`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
