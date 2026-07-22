# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T03:22:28.227396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.1552` n `230`; crypto_major avg `-0.1243` n `8`; equity avg `-0.055` n `98`; fx avg `-0.0101` n `6`; index avg `-0.0327` n `25`; metal avg `0.0161` n `20`; unknown avg `0.0429` n `771`
- 1h: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.2972` n `230`; crypto_major avg `-0.3641` n `8`; equity avg `-0.4371` n `98`; fx avg `0.0133` n `6`; index avg `-0.0832` n `25`; metal avg `0.0901` n `20`; unknown avg `-0.1043` n `771`
- 4h: commodity avg `0.0995` n `12`; crypto_alt avg `0.1106` n `230`; crypto_major avg `0.103` n `8`; equity avg `-0.6172` n `98`; fx avg `0.0271` n `6`; index avg `-0.0434` n `25`; metal avg `0.5068` n `20`; unknown avg `-0.1583` n `771`
- 24h: commodity avg `0.6079` n `12`; crypto_alt avg `0.1517` n `230`; crypto_major avg `-0.0369` n `8`; equity avg `2.7677` n `98`; fx avg `0.0638` n `6`; index avg `0.3556` n `25`; metal avg `0.9704` n `20`; unknown avg `0.3233` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0957`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0596`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0531`, n `666`, weak_sample_signal
