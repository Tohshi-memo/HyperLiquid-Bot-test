# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T20:22:27.964310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0509` n `12`; crypto_alt avg `-0.1109` n `229`; crypto_major avg `-0.0701` n `8`; equity avg `-0.1299` n `91`; fx avg `0.0165` n `6`; index avg `-0.0467` n `25`; metal avg `-0.0485` n `20`; unknown avg `-0.0344` n `764`
- 1h: commodity avg `0.2136` n `12`; crypto_alt avg `-0.0121` n `229`; crypto_major avg `0.1621` n `8`; equity avg `0.2129` n `91`; fx avg `0.0136` n `6`; index avg `-0.0218` n `25`; metal avg `-0.1162` n `20`; unknown avg `-0.0495` n `764`
- 4h: commodity avg `-0.1822` n `12`; crypto_alt avg `0.3713` n `229`; crypto_major avg `0.4574` n `8`; equity avg `0.9225` n `91`; fx avg `-0.0058` n `6`; index avg `0.1066` n `25`; metal avg `0.3393` n `20`; unknown avg `1.3522` n `764`
- 24h: commodity avg `0.489` n `12`; crypto_alt avg `-2.2967` n `229`; crypto_major avg `-2.7924` n `8`; equity avg `0.9025` n `91`; fx avg `0.0058` n `6`; index avg `-0.071` n `25`; metal avg `-0.8449` n `20`; unknown avg `0.0396` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
