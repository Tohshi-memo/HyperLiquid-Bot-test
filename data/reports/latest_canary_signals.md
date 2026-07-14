# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T09:07:33.884902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0988` n `12`; crypto_alt avg `0.0222` n `230`; crypto_major avg `0.0566` n `8`; equity avg `-0.0176` n `92`; fx avg `-0.0033` n `6`; index avg `-0.0048` n `25`; metal avg `0.0233` n `20`; unknown avg `0.0929` n `766`
- 1h: commodity avg `0.0491` n `12`; crypto_alt avg `0.0967` n `230`; crypto_major avg `0.2507` n `8`; equity avg `0.1588` n `92`; fx avg `0.0307` n `6`; index avg `0.0251` n `25`; metal avg `0.0118` n `20`; unknown avg `0.0677` n `766`
- 4h: commodity avg `0.269` n `12`; crypto_alt avg `0.0469` n `230`; crypto_major avg `-0.0388` n `8`; equity avg `0.4966` n `92`; fx avg `0.1028` n `6`; index avg `0.0355` n `25`; metal avg `0.0194` n `20`; unknown avg `0.0408` n `750`
- 24h: commodity avg `1.6997` n `12`; crypto_alt avg `-0.9073` n `230`; crypto_major avg `-0.7799` n `8`; equity avg `-0.534` n `92`; fx avg `-0.0452` n `6`; index avg `-0.1058` n `25`; metal avg `-0.1773` n `20`; unknown avg `-0.293` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
