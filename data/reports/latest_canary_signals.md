# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T17:07:26.148555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `0.0425` n `230`; crypto_major avg `0.114` n `8`; equity avg `0.071` n `92`; fx avg `0.0095` n `6`; index avg `0.0071` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.011` n `765`
- 1h: commodity avg `-0.016` n `12`; crypto_alt avg `0.1929` n `230`; crypto_major avg `0.0629` n `8`; equity avg `0.1263` n `92`; fx avg `0.0079` n `6`; index avg `0.0072` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0747` n `765`
- 4h: commodity avg `-0.0737` n `12`; crypto_alt avg `0.2566` n `230`; crypto_major avg `0.3532` n `8`; equity avg `0.0978` n `92`; fx avg `-0.0214` n `6`; index avg `0.0212` n `25`; metal avg `-0.0201` n `20`; unknown avg `0.0728` n `765`
- 24h: commodity avg `0.1009` n `12`; crypto_alt avg `0.7609` n `229`; crypto_major avg `0.3898` n `8`; equity avg `0.1052` n `92`; fx avg `-0.0508` n `6`; index avg `0.0685` n `25`; metal avg `0.0804` n `20`; unknown avg `2.3025` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
