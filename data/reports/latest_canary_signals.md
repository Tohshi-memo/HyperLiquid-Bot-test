# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T07:35:53.301352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `0.2483` n `230`; crypto_major avg `0.2694` n `8`; equity avg `-0.0411` n `92`; fx avg `0.0008` n `6`; index avg `0.0006` n `25`; metal avg `0.0471` n `20`; unknown avg `0.0277` n `766`
- 1h: commodity avg `-0.0354` n `12`; crypto_alt avg `0.3414` n `230`; crypto_major avg `0.4399` n `8`; equity avg `0.249` n `92`; fx avg `0.0063` n `6`; index avg `0.0578` n `25`; metal avg `0.086` n `20`; unknown avg `0.0554` n `766`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `1.1212` n `230`; crypto_major avg `0.4131` n `8`; equity avg `-0.1116` n `92`; fx avg `-0.0249` n `6`; index avg `-0.0289` n `25`; metal avg `0.1948` n `20`; unknown avg `0.044` n `750`
- 24h: commodity avg `-0.0347` n `12`; crypto_alt avg `-0.8989` n `230`; crypto_major avg `-0.6555` n `8`; equity avg `-2.3085` n `92`; fx avg `0.0155` n `6`; index avg `-0.4738` n `25`; metal avg `-0.3153` n `20`; unknown avg `-0.02` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
