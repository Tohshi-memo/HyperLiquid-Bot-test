# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T23:50:00.646334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0339` n `12`; crypto_alt avg `-0.0464` n `228`; crypto_major avg `-0.066` n `8`; equity avg `-0.0355` n `66`; fx avg `-0.0029` n `6`; index avg `0.0565` n `23`; metal avg `0.0646` n `18`; unknown avg `-0.0105` n `383`
- 1h: commodity avg `-0.098` n `12`; crypto_alt avg `0.2929` n `228`; crypto_major avg `0.2933` n `8`; equity avg `0.2022` n `66`; fx avg `-0.0106` n `6`; index avg `0.2371` n `23`; metal avg `0.3443` n `18`; unknown avg `0.015` n `383`
- 4h: commodity avg `-0.1467` n `12`; crypto_alt avg `-0.0551` n `228`; crypto_major avg `-0.0492` n `8`; equity avg `0.1176` n `66`; fx avg `-0.0534` n `6`; index avg `0.1703` n `23`; metal avg `0.2816` n `18`; unknown avg `0.085` n `383`
- 24h: commodity avg `1.0034` n `12`; crypto_alt avg `-1.0473` n `228`; crypto_major avg `-0.53` n `8`; equity avg `-0.1757` n `66`; fx avg `0.0187` n `6`; index avg `-0.4834` n `23`; metal avg `-2.8121` n `18`; unknown avg `0.7817` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
