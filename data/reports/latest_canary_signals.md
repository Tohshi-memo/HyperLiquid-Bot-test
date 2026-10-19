# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T07:22:30.893226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0306` n `13`; crypto_alt avg `0.0298` n `237`; crypto_major avg `-0.0518` n `8`; equity avg `-0.0991` n `151`; fx avg `-0.0066` n `6`; index avg `-0.0228` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.6272` n `1192`
- 1h: commodity avg `0.012` n `13`; crypto_alt avg `0.1523` n `237`; crypto_major avg `0.1322` n `8`; equity avg `-0.226` n `151`; fx avg `-0.0173` n `6`; index avg `-0.0409` n `26`; metal avg `0.0132` n `20`; unknown avg `0.2129` n `1190`
- 4h: commodity avg `-0.1069` n `13`; crypto_alt avg `0.1842` n `237`; crypto_major avg `0.3125` n `8`; equity avg `0.0231` n `151`; fx avg `-0.0424` n `6`; index avg `0.0019` n `26`; metal avg `0.0057` n `20`; unknown avg `5.8326` n `1162`
- 24h: commodity avg `-0.471` n `13`; crypto_alt avg `0.5328` n `237`; crypto_major avg `1.2733` n `8`; equity avg `2.7325` n `151`; fx avg `-0.0459` n `6`; index avg `0.4885` n `26`; metal avg `0.3206` n `20`; unknown avg `2.5921` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1939`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1173`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0676`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0643`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0606`, n `666`, weak_sample_signal
