# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T07:52:27.078384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0986` n `12`; crypto_alt avg `0.1062` n `228`; crypto_major avg `0.1113` n `8`; equity avg `-0.0261` n `74`; fx avg `0.0238` n `6`; index avg `-0.0393` n `23`; metal avg `0.0913` n `18`; unknown avg `-0.0809` n `547`
- 1h: commodity avg `0.2056` n `12`; crypto_alt avg `0.025` n `228`; crypto_major avg `-0.0806` n `8`; equity avg `-0.1297` n `74`; fx avg `0.0336` n `6`; index avg `-0.0686` n `23`; metal avg `-0.0775` n `18`; unknown avg `0.1102` n `547`
- 4h: commodity avg `0.1845` n `12`; crypto_alt avg `1.5352` n `228`; crypto_major avg `0.8889` n `8`; equity avg `0.4197` n `74`; fx avg `0.0386` n `6`; index avg `0.1487` n `23`; metal avg `0.3213` n `18`; unknown avg `0.2389` n `503`
- 24h: commodity avg `-1.1085` n `12`; crypto_alt avg `0.1144` n `228`; crypto_major avg `0.3867` n `8`; equity avg `2.2708` n `74`; fx avg `-0.0538` n `6`; index avg `0.9262` n `23`; metal avg `0.7955` n `18`; unknown avg `-2.8874` n `503`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
