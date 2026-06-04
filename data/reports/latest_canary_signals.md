# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T06:37:24.420472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2164` n `12`; crypto_alt avg `-0.0774` n `228`; crypto_major avg `-0.2981` n `8`; equity avg `0.1175` n `73`; fx avg `0.0138` n `6`; index avg `0.0528` n `23`; metal avg `0.0224` n `18`; unknown avg `-0.0375` n `424`
- 1h: commodity avg `-0.1941` n `12`; crypto_alt avg `0.7297` n `228`; crypto_major avg `0.0234` n `8`; equity avg `0.0801` n `73`; fx avg `0.0237` n `6`; index avg `0.0464` n `23`; metal avg `-0.1072` n `18`; unknown avg `2.1348` n `404`
- 4h: commodity avg `-0.0923` n `12`; crypto_alt avg `0.9755` n `228`; crypto_major avg `0.7515` n `8`; equity avg `0.6207` n `73`; fx avg `0.0185` n `6`; index avg `0.2418` n `23`; metal avg `0.0546` n `18`; unknown avg `0.6818` n `404`
- 24h: commodity avg `-0.2372` n `12`; crypto_alt avg `-4.2166` n `228`; crypto_major avg `-3.8339` n `8`; equity avg `-3.6207` n `73`; fx avg `-0.0505` n `6`; index avg `-1.039` n `23`; metal avg `-1.2618` n `18`; unknown avg `0.0588` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
