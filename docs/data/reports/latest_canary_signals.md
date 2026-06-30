# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T17:19:48.795519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.2062` n `228`; crypto_major avg `-0.2161` n `8`; equity avg `-0.062` n `88`; fx avg `-0.0097` n `6`; index avg `-0.0049` n `23`; metal avg `0.0116` n `20`; unknown avg `-0.0544` n `765`
- 1h: commodity avg `-0.0963` n `12`; crypto_alt avg `0.1758` n `228`; crypto_major avg `0.3898` n `8`; equity avg `0.1565` n `88`; fx avg `-0.0185` n `6`; index avg `0.0251` n `23`; metal avg `-0.1111` n `20`; unknown avg `0.2683` n `765`
- 4h: commodity avg `-0.1379` n `12`; crypto_alt avg `0.6464` n `228`; crypto_major avg `0.5268` n `8`; equity avg `1.2506` n `88`; fx avg `0.0507` n `6`; index avg `0.2602` n `23`; metal avg `-0.0492` n `20`; unknown avg `0.1425` n `765`
- 24h: commodity avg `0.0371` n `12`; crypto_alt avg `-2.5333` n `228`; crypto_major avg `-2.4275` n `8`; equity avg `1.3954` n `88`; fx avg `0.1229` n `6`; index avg `0.3798` n `23`; metal avg `0.3593` n `20`; unknown avg `8.7414` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
