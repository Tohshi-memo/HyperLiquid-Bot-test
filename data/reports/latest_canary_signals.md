# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T02:22:29.961518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.2433` n `230`; crypto_major avg `-0.2252` n `8`; equity avg `-0.2828` n `92`; fx avg `0.011` n `6`; index avg `-0.1007` n `25`; metal avg `0.0567` n `20`; unknown avg `-0.0274` n `766`
- 1h: commodity avg `-0.0479` n `12`; crypto_alt avg `-0.433` n `230`; crypto_major avg `-0.3497` n `8`; equity avg `-0.6787` n `92`; fx avg `0.0507` n `6`; index avg `-0.203` n `25`; metal avg `0.1494` n `20`; unknown avg `-0.212` n `766`
- 4h: commodity avg `0.149` n `12`; crypto_alt avg `0.3713` n `230`; crypto_major avg `0.3153` n `8`; equity avg `-0.4283` n `92`; fx avg `-0.0233` n `6`; index avg `-0.16` n `25`; metal avg `0.044` n `20`; unknown avg `0.0415` n `766`
- 24h: commodity avg `0.8618` n `12`; crypto_alt avg `-1.3347` n `230`; crypto_major avg `-1.872` n `8`; equity avg `-2.1651` n `92`; fx avg `-0.1309` n `6`; index avg `-0.4592` n `25`; metal avg `-0.1983` n `20`; unknown avg `-0.4258` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
