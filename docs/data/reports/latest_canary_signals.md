# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T21:37:41.738871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.2165` n `228`; crypto_major avg `0.0973` n `8`; equity avg `0.0194` n `88`; fx avg `0.0134` n `6`; index avg `0.0011` n `23`; metal avg `-0.003` n `20`; unknown avg `0.0287` n `765`
- 1h: commodity avg `0.0262` n `12`; crypto_alt avg `-0.0347` n `228`; crypto_major avg `-0.1653` n `8`; equity avg `0.0485` n `88`; fx avg `-0.0075` n `6`; index avg `0.0003` n `23`; metal avg `-0.0557` n `20`; unknown avg `-0.165` n `765`
- 4h: commodity avg `0.005` n `12`; crypto_alt avg `-0.2771` n `228`; crypto_major avg `0.1186` n `8`; equity avg `0.3773` n `88`; fx avg `-0.0068` n `6`; index avg `-0.0462` n `23`; metal avg `-0.2` n `20`; unknown avg `1.1759` n `763`
- 24h: commodity avg `0.1452` n `12`; crypto_alt avg `-2.4425` n `228`; crypto_major avg `-2.5223` n `8`; equity avg `1.178` n `88`; fx avg `0.1134` n `6`; index avg `0.2047` n `23`; metal avg `-0.073` n `20`; unknown avg `7.5317` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
