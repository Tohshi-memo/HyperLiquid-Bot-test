# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T23:22:27.594069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.032` n `229`; crypto_major avg `0.0503` n `8`; equity avg `0.0553` n `92`; fx avg `0.0078` n `6`; index avg `-0.002` n `25`; metal avg `0.0055` n `20`; unknown avg `0.2876` n `765`
- 1h: commodity avg `0.0111` n `12`; crypto_alt avg `0.005` n `229`; crypto_major avg `0.0311` n `8`; equity avg `0.048` n `92`; fx avg `0.0022` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0047` n `20`; unknown avg `0.284` n `765`
- 4h: commodity avg `-0.0291` n `12`; crypto_alt avg `0.5641` n `229`; crypto_major avg `0.384` n `8`; equity avg `0.0083` n `92`; fx avg `-0.0062` n `6`; index avg `0.001` n `25`; metal avg `0.0916` n `20`; unknown avg `-0.2234` n `765`
- 24h: commodity avg `-0.2371` n `12`; crypto_alt avg `1.2439` n `229`; crypto_major avg `1.1231` n `8`; equity avg `-0.7545` n `92`; fx avg `-0.167` n `6`; index avg `0.0158` n `25`; metal avg `0.132` n `20`; unknown avg `-0.2231` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
