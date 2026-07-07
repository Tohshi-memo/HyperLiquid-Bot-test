# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T23:22:25.036083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.092` n `229`; crypto_major avg `0.1057` n `8`; equity avg `0.0328` n `91`; fx avg `0.012` n `6`; index avg `0.0193` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.0114` n `763`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `0.3398` n `229`; crypto_major avg `0.3644` n `8`; equity avg `-0.1485` n `91`; fx avg `0.0144` n `6`; index avg `-0.0112` n `25`; metal avg `0.0087` n `20`; unknown avg `0.0498` n `763`
- 4h: commodity avg `0.0846` n `12`; crypto_alt avg `-0.2331` n `229`; crypto_major avg `0.0391` n `8`; equity avg `-0.0706` n `91`; fx avg `0.0024` n `6`; index avg `0.0277` n `25`; metal avg `0.0292` n `20`; unknown avg `0.048` n `763`
- 24h: commodity avg `0.9145` n `12`; crypto_alt avg `-2.5411` n `229`; crypto_major avg `-1.4343` n `8`; equity avg `-3.2821` n `91`; fx avg `-0.2517` n `6`; index avg `-0.5886` n `25`; metal avg `-0.6316` n `20`; unknown avg `0.0322` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
