# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T00:07:12.569390+00:00`
- Correlation status: `ready`
- Asset price records: `596`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1024` n `12`; crypto_alt avg `0.0833` n `228`; crypto_major avg `0.068` n `8`; equity avg `0.114` n `65`; fx avg `0.0512` n `5`; index avg `0.1194` n `23`; metal avg `0.1549` n `18`; unknown avg `-0.0406` n `365`
- 1h: commodity avg `-0.2124` n `12`; crypto_alt avg `0.3509` n `228`; crypto_major avg `0.1718` n `8`; equity avg `0.314` n `65`; fx avg `0.0505` n `5`; index avg `0.2074` n `23`; metal avg `0.4972` n `18`; unknown avg `-0.0296` n `365`
- 4h: commodity avg `0.594` n `12`; crypto_alt avg `-0.0482` n `228`; crypto_major avg `-0.2073` n `8`; equity avg `-0.5758` n `65`; fx avg `0.0056` n `5`; index avg `0.1684` n `23`; metal avg `-0.2599` n `18`; unknown avg `-0.3937` n `365`
- 24h: commodity avg `0.4664` n `12`; crypto_alt avg `1.5495` n `228`; crypto_major avg `-1.7136` n `8`; equity avg `-1.1767` n `65`; fx avg `0.1496` n `5`; index avg `-0.6768` n `23`; metal avg `0.1903` n `18`; unknown avg `-0.3893` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.137`, n `592`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `592`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `592`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `592`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `588`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `588`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0836`, n `588`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0826`, n `588`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0786`, n `588`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0751`, n `588`, weak_sample_signal
