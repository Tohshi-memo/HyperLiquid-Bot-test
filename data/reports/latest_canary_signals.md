# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T22:07:28.160831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.1159` n `230`; crypto_major avg `-0.0847` n `8`; equity avg `-0.0656` n `113`; fx avg `-0.0054` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0446` n `20`; unknown avg `0.0322` n `786`
- 1h: commodity avg `-0.013` n `12`; crypto_alt avg `-0.8011` n `230`; crypto_major avg `-0.4267` n `8`; equity avg `-0.0104` n `113`; fx avg `-0.0072` n `6`; index avg `0.0188` n `25`; metal avg `-0.0649` n `20`; unknown avg `-0.0274` n `786`
- 4h: commodity avg `-0.0738` n `12`; crypto_alt avg `-1.1802` n `230`; crypto_major avg `-0.613` n `8`; equity avg `-0.3657` n `113`; fx avg `-0.0146` n `6`; index avg `0.0139` n `25`; metal avg `-0.0629` n `20`; unknown avg `-0.3747` n `786`
- 24h: commodity avg `-0.0196` n `12`; crypto_alt avg `-1.8064` n `230`; crypto_major avg `-0.7583` n `8`; equity avg `2.8803` n `113`; fx avg `0.0154` n `6`; index avg `0.4117` n `25`; metal avg `0.074` n `20`; unknown avg `-0.1496` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2346`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1877`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
