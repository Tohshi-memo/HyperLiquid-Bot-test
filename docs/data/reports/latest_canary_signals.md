# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T21:52:33.811902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `0.0759` n `230`; crypto_major avg `0.0749` n `8`; equity avg `0.008` n `108`; fx avg `0.0017` n `6`; index avg `0.0006` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0873` n `782`
- 1h: commodity avg `0.0898` n `12`; crypto_alt avg `-0.3193` n `230`; crypto_major avg `-0.4153` n `8`; equity avg `-0.2211` n `108`; fx avg `0.008` n `6`; index avg `-0.0154` n `25`; metal avg `0.0261` n `20`; unknown avg `0.0681` n `782`
- 4h: commodity avg `0.1225` n `12`; crypto_alt avg `-0.3645` n `230`; crypto_major avg `-0.5135` n `8`; equity avg `-1.2619` n `108`; fx avg `0.0117` n `6`; index avg `-0.1368` n `25`; metal avg `-0.0336` n `20`; unknown avg `-0.001` n `782`
- 24h: commodity avg `0.06` n `12`; crypto_alt avg `0.3793` n `230`; crypto_major avg `0.6033` n `8`; equity avg `-0.8702` n `108`; fx avg `-0.0479` n `6`; index avg `-0.1404` n `25`; metal avg `0.8046` n `20`; unknown avg `0.7132` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
