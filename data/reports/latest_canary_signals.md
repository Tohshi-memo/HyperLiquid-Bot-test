# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T05:37:25.718883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0579` n `12`; crypto_alt avg `0.1179` n `230`; crypto_major avg `0.172` n `8`; equity avg `-0.0485` n `93`; fx avg `-0.0015` n `6`; index avg `-0.007` n `25`; metal avg `0.0106` n `20`; unknown avg `0.1229` n `767`
- 1h: commodity avg `-0.0613` n `12`; crypto_alt avg `-0.0676` n `230`; crypto_major avg `-0.0473` n `8`; equity avg `-0.3011` n `93`; fx avg `-0.0266` n `6`; index avg `-0.0472` n `25`; metal avg `-0.0407` n `20`; unknown avg `-0.2654` n `767`
- 4h: commodity avg `-0.0962` n `12`; crypto_alt avg `-0.2427` n `230`; crypto_major avg `0.2805` n `8`; equity avg `0.7313` n `93`; fx avg `0.0217` n `6`; index avg `0.0783` n `25`; metal avg `-0.0989` n `20`; unknown avg `-0.3217` n `767`
- 24h: commodity avg `0.1551` n `12`; crypto_alt avg `1.4105` n `230`; crypto_major avg `2.9283` n `8`; equity avg `1.5255` n `92`; fx avg `0.0933` n `6`; index avg `0.447` n `25`; metal avg `0.1546` n `20`; unknown avg `0.3328` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
