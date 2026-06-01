# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T08:22:19.149397+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1033` n `12`; crypto_alt avg `0.0036` n `228`; crypto_major avg `-0.0445` n `8`; equity avg `-0.041` n `69`; fx avg `0.0044` n `6`; index avg `-0.0212` n `23`; metal avg `-0.1473` n `18`; unknown avg `-0.011` n `422`
- 1h: commodity avg `0.0672` n `12`; crypto_alt avg `-0.4981` n `228`; crypto_major avg `-0.4085` n `8`; equity avg `-0.3012` n `69`; fx avg `-0.0046` n `6`; index avg `-0.5963` n `23`; metal avg `-0.2174` n `18`; unknown avg `-0.1268` n `422`
- 4h: commodity avg `0.3808` n `12`; crypto_alt avg `-1.6714` n `228`; crypto_major avg `-0.9727` n `8`; equity avg `-0.439` n `69`; fx avg `-0.0284` n `6`; index avg `-0.2759` n `23`; metal avg `-0.3064` n `18`; unknown avg `-0.0988` n `412`
- 24h: commodity avg `1.3196` n `12`; crypto_alt avg `-0.8364` n `228`; crypto_major avg `-1.3009` n `8`; equity avg `-0.3323` n `69`; fx avg `-0.0123` n `6`; index avg `0.3832` n `23`; metal avg `-0.1258` n `18`; unknown avg `1.5352` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2874`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
