# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T07:07:29.799698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `-0.3786` n `233`; crypto_major avg `-0.4061` n `8`; equity avg `-0.0609` n `134`; fx avg `-0.0219` n `6`; index avg `-0.0181` n `26`; metal avg `-0.0824` n `20`; unknown avg `0.2982` n `795`
- 1h: commodity avg `0.0937` n `12`; crypto_alt avg `-0.2551` n `233`; crypto_major avg `-0.3517` n `8`; equity avg `-0.0916` n `134`; fx avg `0.0159` n `6`; index avg `-0.0105` n `26`; metal avg `-0.1054` n `20`; unknown avg `0.5747` n `793`
- 4h: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.2678` n `233`; crypto_major avg `-0.5335` n `8`; equity avg `0.1052` n `134`; fx avg `0.0153` n `6`; index avg `0.0624` n `26`; metal avg `-0.0469` n `20`; unknown avg `0.2464` n `765`
- 24h: commodity avg `-0.073` n `12`; crypto_alt avg `-4.2155` n `233`; crypto_major avg `-3.1794` n `8`; equity avg `-1.1674` n `134`; fx avg `0.0815` n `6`; index avg `-0.1336` n `26`; metal avg `0.1832` n `20`; unknown avg `0.5213` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
