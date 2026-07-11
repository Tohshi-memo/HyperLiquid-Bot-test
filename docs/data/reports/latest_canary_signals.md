# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T19:37:24.445251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `-0.0867` n `230`; crypto_major avg `-0.1027` n `8`; equity avg `0.0301` n `92`; fx avg `0.0076` n `6`; index avg `0.0025` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0375` n `765`
- 1h: commodity avg `-0.0302` n `12`; crypto_alt avg `-0.103` n `230`; crypto_major avg `-0.1036` n `8`; equity avg `0.0093` n `92`; fx avg `-0.0022` n `6`; index avg `0.0003` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0663` n `765`
- 4h: commodity avg `0.0098` n `12`; crypto_alt avg `0.3541` n `230`; crypto_major avg `0.1648` n `8`; equity avg `0.2224` n `92`; fx avg `0.0005` n `6`; index avg `0.0034` n `25`; metal avg `0.0028` n `20`; unknown avg `0.0533` n `765`
- 24h: commodity avg `-0.0017` n `12`; crypto_alt avg `0.9864` n `229`; crypto_major avg `0.6159` n `8`; equity avg `0.2502` n `92`; fx avg `0.0003` n `6`; index avg `0.0368` n `25`; metal avg `0.0764` n `20`; unknown avg `2.3248` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
