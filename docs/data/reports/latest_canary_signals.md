# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T13:52:16.787650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0909` n `12`; crypto_alt avg `0.0965` n `228`; crypto_major avg `-0.0426` n `8`; equity avg `-0.4195` n `66`; fx avg `0.0034` n `6`; index avg `-0.3647` n `23`; metal avg `0.4219` n `18`; unknown avg `-0.2608` n `383`
- 1h: commodity avg `0.1705` n `12`; crypto_alt avg `0.4594` n `228`; crypto_major avg `0.1864` n `8`; equity avg `0.1047` n `66`; fx avg `0.0028` n `6`; index avg `-0.2945` n `23`; metal avg `-0.9981` n `18`; unknown avg `-0.185` n `383`
- 4h: commodity avg `0.2802` n `12`; crypto_alt avg `0.1709` n `228`; crypto_major avg `0.3696` n `8`; equity avg `0.0942` n `66`; fx avg `-0.0543` n `6`; index avg `-0.2086` n `23`; metal avg `-1.0152` n `18`; unknown avg `-0.741` n `383`
- 24h: commodity avg `2.0704` n `12`; crypto_alt avg `0.7261` n `228`; crypto_major avg `0.4682` n `8`; equity avg `-1.6417` n `66`; fx avg `0.2166` n `6`; index avg `-1.3025` n `23`; metal avg `-2.3459` n `18`; unknown avg `0.0612` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
