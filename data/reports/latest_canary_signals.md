# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T23:11:01.061502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.1418` n `230`; crypto_major avg `-0.0414` n `8`; equity avg `-0.1006` n `98`; fx avg `0.0034` n `6`; index avg `0.0129` n `25`; metal avg `-0.0129` n `20`; unknown avg `-0.1088` n `769`
- 1h: commodity avg `-0.0601` n `12`; crypto_alt avg `0.4014` n `230`; crypto_major avg `0.3626` n `8`; equity avg `0.2083` n `98`; fx avg `0.0065` n `6`; index avg `0.0692` n `25`; metal avg `0.02` n `20`; unknown avg `-0.1795` n `769`
- 4h: commodity avg `-0.0144` n `12`; crypto_alt avg `0.4132` n `230`; crypto_major avg `0.3792` n `8`; equity avg `0.1995` n `98`; fx avg `0.0186` n `6`; index avg `0.073` n `25`; metal avg `-0.1144` n `20`; unknown avg `0.061` n `769`
- 24h: commodity avg `-0.1062` n `12`; crypto_alt avg `-0.0256` n `230`; crypto_major avg `0.3221` n `8`; equity avg `0.5196` n `97`; fx avg `0.0833` n `6`; index avg `0.0155` n `25`; metal avg `-0.0863` n `20`; unknown avg `-0.0867` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1409`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.136`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1266`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0965`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0952`, n `666`, weak_sample_signal
