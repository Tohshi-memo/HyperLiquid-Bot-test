# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T14:37:18.020053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2214` n `12`; crypto_alt avg `-0.2193` n `228`; crypto_major avg `-0.2602` n `8`; equity avg `-0.7884` n `66`; fx avg `0.0178` n `5`; index avg `-0.3067` n `23`; metal avg `-0.2311` n `18`; unknown avg `-0.2719` n `384`
- 1h: commodity avg `0.7252` n `12`; crypto_alt avg `-0.2741` n `228`; crypto_major avg `-0.2886` n `8`; equity avg `-1.2882` n `66`; fx avg `0.0335` n `5`; index avg `-0.5035` n `23`; metal avg `-0.6563` n `18`; unknown avg `-0.1643` n `383`
- 4h: commodity avg `-0.3418` n `12`; crypto_alt avg `0.303` n `228`; crypto_major avg `-0.1554` n `8`; equity avg `-1.072` n `66`; fx avg `-0.0185` n `5`; index avg `-0.2058` n `23`; metal avg `0.4264` n `18`; unknown avg `0.2812` n `383`
- 24h: commodity avg `0.5803` n `12`; crypto_alt avg `-2.4723` n `228`; crypto_major avg `-1.6243` n `8`; equity avg `-1.2044` n `65`; fx avg `0.0745` n `5`; index avg `-0.2214` n `23`; metal avg `0.3233` n `18`; unknown avg `-0.2898` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
