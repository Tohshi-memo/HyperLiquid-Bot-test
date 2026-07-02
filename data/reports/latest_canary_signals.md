# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T08:22:31.428672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `0.0137` n `228`; crypto_major avg `-0.0133` n `8`; equity avg `0.0894` n `88`; fx avg `-0.004` n `6`; index avg `0.0184` n `25`; metal avg `0.1391` n `20`; unknown avg `-0.0145` n `763`
- 1h: commodity avg `0.1097` n `12`; crypto_alt avg `0.4149` n `228`; crypto_major avg `0.3546` n `8`; equity avg `0.3889` n `88`; fx avg `-0.0238` n `6`; index avg `0.0503` n `25`; metal avg `0.1661` n `20`; unknown avg `0.6484` n `763`
- 4h: commodity avg `0.0144` n `12`; crypto_alt avg `-0.0324` n `228`; crypto_major avg `-0.4146` n `8`; equity avg `-0.8279` n `88`; fx avg `-0.0499` n `6`; index avg `-0.174` n `25`; metal avg `0.0019` n `20`; unknown avg `1.0708` n `741`
- 24h: commodity avg `-0.4311` n `12`; crypto_alt avg `2.5072` n `228`; crypto_major avg `1.9975` n `8`; equity avg `-2.1304` n `88`; fx avg `-0.0612` n `6`; index avg `-0.5506` n `25`; metal avg `1.1347` n `20`; unknown avg `15.8893` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
