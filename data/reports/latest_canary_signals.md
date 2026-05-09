# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T08:07:19.198780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.075` n `12`; crypto_alt avg `0.2616` n `228`; crypto_major avg `0.097` n `8`; equity avg `0.1727` n `65`; fx avg `0.0` n `5`; index avg `-0.0319` n `23`; metal avg `-0.0155` n `18`; unknown avg `-0.0164` n `376`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.0381` n `228`; crypto_major avg `0.0716` n `8`; equity avg `0.0792` n `65`; fx avg `0.0017` n `5`; index avg `-0.0148` n `23`; metal avg `0.0027` n `18`; unknown avg `0.1437` n `376`
- 4h: commodity avg `0.0357` n `12`; crypto_alt avg `-0.3729` n `228`; crypto_major avg `-0.4525` n `8`; equity avg `0.0784` n `65`; fx avg `0.0198` n `5`; index avg `-0.0146` n `23`; metal avg `-0.019` n `18`; unknown avg `-0.3242` n `355`
- 24h: commodity avg `-0.1779` n `12`; crypto_alt avg `3.9764` n `228`; crypto_major avg `2.479` n `8`; equity avg `2.9718` n `65`; fx avg `-0.0059` n `5`; index avg `1.1982` n `23`; metal avg `0.1191` n `18`; unknown avg `1.0135` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
