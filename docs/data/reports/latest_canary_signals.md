# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T07:07:36.109169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0414` n `13`; crypto_alt avg `0.3822` n `235`; crypto_major avg `0.3465` n `8`; equity avg `0.0926` n `144`; fx avg `-0.0021` n `6`; index avg `0.0309` n `26`; metal avg `0.0551` n `20`; unknown avg `-0.2463` n `1077`
- 1h: commodity avg `0.0516` n `13`; crypto_alt avg `0.5423` n `235`; crypto_major avg `0.553` n `8`; equity avg `0.0569` n `144`; fx avg `0.0069` n `6`; index avg `0.0207` n `26`; metal avg `0.079` n `20`; unknown avg `-0.2417` n `1077`
- 4h: commodity avg `0.0074` n `13`; crypto_alt avg `0.2217` n `235`; crypto_major avg `0.1958` n `8`; equity avg `0.0192` n `144`; fx avg `0.0227` n `6`; index avg `0.0032` n `26`; metal avg `0.1638` n `20`; unknown avg `-0.0399` n `970`
- 24h: commodity avg `-0.3216` n `13`; crypto_alt avg `0.9013` n `235`; crypto_major avg `1.474` n `8`; equity avg `0.3235` n `144`; fx avg `-0.0791` n `6`; index avg `-0.0244` n `26`; metal avg `0.2052` n `20`; unknown avg `-0.0992` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
