# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T16:36:35.159762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `0.1536` n `230`; crypto_major avg `0.1386` n `8`; equity avg `0.0073` n `121`; fx avg `0.0018` n `6`; index avg `-0.0014` n `25`; metal avg `-0.009` n `20`; unknown avg `0.0395` n `794`
- 1h: commodity avg `0.0271` n `12`; crypto_alt avg `0.7957` n `230`; crypto_major avg `0.6333` n `8`; equity avg `0.0567` n `121`; fx avg `0.0201` n `6`; index avg `0.0027` n `25`; metal avg `0.0015` n `20`; unknown avg `0.1356` n `794`
- 4h: commodity avg `-0.0485` n `12`; crypto_alt avg `-0.1797` n `230`; crypto_major avg `-0.3583` n `8`; equity avg `-0.0422` n `121`; fx avg `0.0065` n `6`; index avg `-0.0093` n `25`; metal avg `0.012` n `20`; unknown avg `0.175` n `794`
- 24h: commodity avg `-0.065` n `12`; crypto_alt avg `0.5216` n `230`; crypto_major avg `2.7027` n `8`; equity avg `-0.5173` n `121`; fx avg `0.0622` n `6`; index avg `-0.0691` n `25`; metal avg `-0.1479` n `20`; unknown avg `0.4815` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
