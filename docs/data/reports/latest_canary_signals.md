# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T11:22:29.509193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0902` n `12`; crypto_alt avg `0.0294` n `230`; crypto_major avg `0.022` n `8`; equity avg `0.1384` n `92`; fx avg `0.001` n `6`; index avg `0.044` n `25`; metal avg `0.0283` n `20`; unknown avg `0.0047` n `766`
- 1h: commodity avg `-0.0656` n `12`; crypto_alt avg `0.0383` n `230`; crypto_major avg `0.1764` n `8`; equity avg `-0.2258` n `92`; fx avg `0.017` n `6`; index avg `0.0294` n `25`; metal avg `-0.0098` n `20`; unknown avg `0.022` n `766`
- 4h: commodity avg `0.0427` n `12`; crypto_alt avg `-0.1488` n `230`; crypto_major avg `0.293` n `8`; equity avg `-0.0296` n `92`; fx avg `0.0704` n `6`; index avg `0.046` n `25`; metal avg `-0.113` n `20`; unknown avg `-0.0968` n `766`
- 24h: commodity avg `1.3534` n `12`; crypto_alt avg `-1.0329` n `230`; crypto_major avg `-0.4958` n `8`; equity avg `-0.8249` n `92`; fx avg `-0.0125` n `6`; index avg `-0.0802` n `25`; metal avg `-0.1448` n `20`; unknown avg `-0.3189` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
