# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T20:37:27.604855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.1815` n `228`; crypto_major avg `-0.0551` n `8`; equity avg `-0.0125` n `88`; fx avg `-0.0116` n `6`; index avg `-0.0135` n `23`; metal avg `-0.0797` n `20`; unknown avg `-0.0526` n `765`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.3715` n `228`; crypto_major avg `-0.2811` n `8`; equity avg `0.0803` n `88`; fx avg `0.0035` n `6`; index avg `-0.0343` n `23`; metal avg `-0.1711` n `20`; unknown avg `1.6239` n `763`
- 4h: commodity avg `-0.1671` n `12`; crypto_alt avg `0.0256` n `228`; crypto_major avg `0.7124` n `8`; equity avg `0.4867` n `88`; fx avg `-0.0` n `6`; index avg `-0.0326` n `23`; metal avg `-0.2247` n `20`; unknown avg `1.4208` n `763`
- 24h: commodity avg `0.1056` n `12`; crypto_alt avg `-2.4807` n `228`; crypto_major avg `-2.2793` n `8`; equity avg `1.2242` n `88`; fx avg `0.1397` n `6`; index avg `0.2369` n `23`; metal avg `0.007` n `20`; unknown avg `8.0428` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
