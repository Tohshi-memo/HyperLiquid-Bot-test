# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T07:07:25.378489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `-0.0144` n `230`; crypto_major avg `-0.0305` n `8`; equity avg `0.0681` n `92`; fx avg `0.0103` n `6`; index avg `0.0145` n `25`; metal avg `0.0228` n `20`; unknown avg `0.0353` n `766`
- 1h: commodity avg `-0.1498` n `12`; crypto_alt avg `0.0685` n `230`; crypto_major avg `-0.1301` n `8`; equity avg `-0.1505` n `92`; fx avg `-0.0445` n `6`; index avg `0.015` n `25`; metal avg `0.1208` n `20`; unknown avg `0.1411` n `766`
- 4h: commodity avg `-0.0621` n `12`; crypto_alt avg `0.3661` n `230`; crypto_major avg `-0.4328` n `8`; equity avg `-0.4832` n `92`; fx avg `-0.0147` n `6`; index avg `-0.0955` n `25`; metal avg `0.0692` n `20`; unknown avg `-0.023` n `750`
- 24h: commodity avg `0.0348` n `12`; crypto_alt avg `-1.2513` n `230`; crypto_major avg `-1.0662` n `8`; equity avg `-2.3777` n `92`; fx avg `0.02` n `6`; index avg `-0.4841` n `25`; metal avg `-0.4018` n `20`; unknown avg `-0.0601` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
