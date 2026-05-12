# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-12T03:07:23.507617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3005` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.5258` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0503` n `12`; crypto_alt avg `0.2175` n `228`; crypto_major avg `-0.1044` n `8`; equity avg `0.2645` n `65`; fx avg `-0.0143` n `5`; index avg `0.0989` n `23`; metal avg `0.0972` n `18`; unknown avg `-0.1267` n `377`
- 1h: commodity avg `0.0503` n `12`; crypto_alt avg `0.2175` n `228`; crypto_major avg `-0.1044` n `8`; equity avg `0.2645` n `65`; fx avg `-0.0143` n `5`; index avg `0.0989` n `23`; metal avg `0.0972` n `18`; unknown avg `-0.1267` n `377`
- 4h: commodity avg `2.8479` n `12`; crypto_alt avg `-0.3028` n `228`; crypto_major avg `0.5474` n `8`; equity avg `-0.9784` n `65`; fx avg `0.4099` n `5`; index avg `-0.1288` n `23`; metal avg `1.986` n `18`; unknown avg `-0.2877` n `366`
- 24h: commodity avg `2.8479` n `12`; crypto_alt avg `-0.3028` n `228`; crypto_major avg `0.5474` n `8`; equity avg `-0.9784` n `65`; fx avg `0.4099` n `5`; index avg `-0.1288` n `23`; metal avg `1.986` n `18`; unknown avg `-0.2877` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1442`, n `671`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1267`, n `671`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1173`, n `671`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `671`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0964`, n `671`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `671`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `671`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0721`, n `671`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `671`, weak_sample_signal
