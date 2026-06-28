# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T13:22:27.738948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `-0.012` n `228`; crypto_major avg `0.1561` n `8`; equity avg `0.0124` n `88`; fx avg `0.0025` n `6`; index avg `0.0118` n `23`; metal avg `-0.003` n `20`; unknown avg `0.0502` n `764`
- 1h: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.2672` n `228`; crypto_major avg `-0.035` n `8`; equity avg `0.0067` n `88`; fx avg `-0.0017` n `6`; index avg `0.0113` n `23`; metal avg `-0.017` n `20`; unknown avg `-0.0117` n `764`
- 4h: commodity avg `0.0729` n `12`; crypto_alt avg `-0.4157` n `228`; crypto_major avg `-0.2483` n `8`; equity avg `-0.0594` n `88`; fx avg `0.0055` n `6`; index avg `0.012` n `23`; metal avg `-0.0151` n `20`; unknown avg `1.4251` n `750`
- 24h: commodity avg `0.1363` n `12`; crypto_alt avg `-0.534` n `228`; crypto_major avg `-1.0375` n `8`; equity avg `0.0054` n `88`; fx avg `0.001` n `6`; index avg `-0.0496` n `23`; metal avg `-0.0322` n `20`; unknown avg `15.4276` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
