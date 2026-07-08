# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T13:22:29.362275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0463` n `12`; crypto_alt avg `0.1412` n `229`; crypto_major avg `0.0679` n `8`; equity avg `0.0464` n `91`; fx avg `0.0112` n `6`; index avg `-0.005` n `25`; metal avg `0.0197` n `20`; unknown avg `-0.0242` n `764`
- 1h: commodity avg `0.0469` n `12`; crypto_alt avg `-0.4867` n `229`; crypto_major avg `-0.5552` n `8`; equity avg `0.1215` n `91`; fx avg `0.0002` n `6`; index avg `0.0447` n `25`; metal avg `0.0432` n `20`; unknown avg `-0.1459` n `763`
- 4h: commodity avg `-0.3396` n `12`; crypto_alt avg `0.4111` n `229`; crypto_major avg `0.2161` n `8`; equity avg `1.3749` n `91`; fx avg `-0.0322` n `6`; index avg `0.2756` n `25`; metal avg `0.1051` n `20`; unknown avg `0.1159` n `757`
- 24h: commodity avg `1.1526` n `12`; crypto_alt avg `-3.5014` n `229`; crypto_major avg `-3.0432` n `8`; equity avg `-1.9724` n `91`; fx avg `-0.0898` n `6`; index avg `-0.4824` n `25`; metal avg `-1.2761` n `20`; unknown avg `-0.5369` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
