# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T20:50:12.470326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.2123` n `228`; crypto_major avg `0.1715` n `8`; equity avg `0.0425` n `78`; fx avg `0.0341` n `6`; index avg `-0.0015` n `23`; metal avg `0.0472` n `18`; unknown avg `-0.1411` n `687`
- 1h: commodity avg `0.0297` n `12`; crypto_alt avg `0.1176` n `228`; crypto_major avg `-0.015` n `8`; equity avg `0.0349` n `78`; fx avg `-0.016` n `6`; index avg `-0.0031` n `23`; metal avg `0.1003` n `18`; unknown avg `-0.1027` n `687`
- 4h: commodity avg `-0.079` n `12`; crypto_alt avg `-0.1961` n `228`; crypto_major avg `0.1772` n `8`; equity avg `-0.0311` n `78`; fx avg `0.0062` n `6`; index avg `-0.0477` n `23`; metal avg `0.1709` n `18`; unknown avg `-0.0196` n `687`
- 24h: commodity avg `0.3041` n `12`; crypto_alt avg `-3.6966` n `228`; crypto_major avg `-4.5604` n `8`; equity avg `0.706` n `78`; fx avg `-0.1096` n `6`; index avg `0.2183` n `23`; metal avg `-4.1158` n `18`; unknown avg `-0.3437` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
