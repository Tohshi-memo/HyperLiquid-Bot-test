# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T14:22:31.241481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.5937` n `229`; crypto_major avg `-0.4662` n `8`; equity avg `-0.7347` n `88`; fx avg `0.0229` n `6`; index avg `-0.1342` n `25`; metal avg `-0.1058` n `20`; unknown avg `0.0853` n `763`
- 1h: commodity avg `0.0279` n `12`; crypto_alt avg `-0.3089` n `229`; crypto_major avg `0.0328` n `8`; equity avg `-0.1943` n `88`; fx avg `0.0009` n `6`; index avg `-0.0601` n `25`; metal avg `0.1368` n `20`; unknown avg `0.0521` n `763`
- 4h: commodity avg `0.0146` n `12`; crypto_alt avg `0.4977` n `229`; crypto_major avg `1.5538` n `8`; equity avg `1.0626` n `88`; fx avg `0.0365` n `6`; index avg `0.1767` n `25`; metal avg `0.5675` n `20`; unknown avg `-0.4522` n `763`
- 24h: commodity avg `-0.344` n `12`; crypto_alt avg `1.9297` n `228`; crypto_major avg `3.0437` n `8`; equity avg `-1.1468` n `88`; fx avg `-0.0257` n `6`; index avg `-0.3224` n `25`; metal avg `0.4058` n `20`; unknown avg `1.3662` n `739`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
