# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-12T01:52:17.715017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1448` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.8858` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1492` n `12`; crypto_alt avg `-0.9342` n `228`; crypto_major avg `-0.6504` n `8`; equity avg `-1.0353` n `65`; fx avg `0.0616` n `5`; index avg `-0.4472` n `23`; metal avg `-0.6559` n `18`; unknown avg `-0.5778` n `377`
- 1h: commodity avg `0.1492` n `12`; crypto_alt avg `-0.9342` n `228`; crypto_major avg `-0.6504` n `8`; equity avg `-1.0353` n `65`; fx avg `0.0616` n `5`; index avg `-0.4472` n `23`; metal avg `-0.6559` n `18`; unknown avg `-0.5778` n `377`
- 4h: commodity avg `2.7954` n `12`; crypto_alt avg `-0.5153` n `228`; crypto_major avg `0.6506` n `8`; equity avg `-1.2352` n `65`; fx avg `0.4242` n `5`; index avg `-0.2254` n `23`; metal avg `1.8859` n `18`; unknown avg `-0.3437` n `366`
- 24h: commodity avg `2.7954` n `12`; crypto_alt avg `-0.5153` n `228`; crypto_major avg `0.6506` n `8`; equity avg `-1.2352` n `65`; fx avg `0.4242` n `5`; index avg `-0.2254` n `23`; metal avg `1.8859` n `18`; unknown avg `-0.3437` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1442`, n `671`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1272`, n `671`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1165`, n `671`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `671`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `671`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `671`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `671`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.072`, n `671`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `671`, weak_sample_signal
