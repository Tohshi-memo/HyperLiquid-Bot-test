# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T16:37:31.737379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0347` n `12`; crypto_alt avg `0.6256` n `233`; crypto_major avg `0.4807` n `8`; equity avg `0.2052` n `134`; fx avg `0.0003` n `6`; index avg `0.0266` n `26`; metal avg `0.0585` n `20`; unknown avg `0.7169` n `791`
- 1h: commodity avg `-0.1191` n `12`; crypto_alt avg `0.5345` n `233`; crypto_major avg `0.2767` n `8`; equity avg `0.0843` n `134`; fx avg `-0.0055` n `6`; index avg `-0.0224` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.6759` n `789`
- 4h: commodity avg `-0.063` n `12`; crypto_alt avg `-1.041` n `233`; crypto_major avg `-0.994` n `8`; equity avg `0.1796` n `134`; fx avg `0.0096` n `6`; index avg `-0.0332` n `26`; metal avg `0.3921` n `20`; unknown avg `8.3167` n `766`
- 24h: commodity avg `0.4787` n `12`; crypto_alt avg `-1.3647` n `233`; crypto_major avg `-0.4609` n `8`; equity avg `-0.5467` n `134`; fx avg `-0.0878` n `6`; index avg `-0.2206` n `26`; metal avg `0.3417` n `20`; unknown avg `7.224` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
