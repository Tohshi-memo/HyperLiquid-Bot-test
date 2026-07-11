# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T08:37:24.727496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `0.0469` n `230`; crypto_major avg `0.0588` n `8`; equity avg `-0.006` n `92`; fx avg `0.0019` n `6`; index avg `-0.0004` n `25`; metal avg `0.0004` n `20`; unknown avg `0.0071` n `765`
- 1h: commodity avg `0.0192` n `12`; crypto_alt avg `0.1294` n `230`; crypto_major avg `0.1419` n `8`; equity avg `0.0217` n `92`; fx avg `0.0055` n `6`; index avg `0.0033` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.0163` n `765`
- 4h: commodity avg `0.0672` n `12`; crypto_alt avg `-0.0936` n `229`; crypto_major avg `0.0957` n `8`; equity avg `0.1658` n `92`; fx avg `0.0226` n `6`; index avg `0.0101` n `25`; metal avg `-0.0151` n `20`; unknown avg `-0.0041` n `733`
- 24h: commodity avg `-0.1978` n `12`; crypto_alt avg `0.1835` n `229`; crypto_major avg `-0.45` n `8`; equity avg `0.2585` n `92`; fx avg `-0.0867` n `6`; index avg `0.2116` n `25`; metal avg `0.1851` n `20`; unknown avg `2.8989` n `730`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
