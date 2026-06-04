# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T06:22:22.886095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5994` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1362` n `12`; crypto_alt avg `0.5048` n `228`; crypto_major avg `0.266` n `8`; equity avg `-0.1155` n `73`; fx avg `0.0017` n `6`; index avg `-0.0052` n `23`; metal avg `-0.1441` n `18`; unknown avg `0.0515` n `424`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `1.3052` n `228`; crypto_major avg `0.8239` n `8`; equity avg `0.1553` n `73`; fx avg `0.0057` n `6`; index avg `0.0122` n `23`; metal avg `-0.1851` n `18`; unknown avg `0.1154` n `404`
- 4h: commodity avg `0.1658` n `12`; crypto_alt avg `1.5419` n `228`; crypto_major avg `1.5963` n `8`; equity avg `0.753` n `73`; fx avg `0.0222` n `6`; index avg `0.2105` n `23`; metal avg `-0.0031` n `18`; unknown avg `1.0515` n `404`
- 24h: commodity avg `-0.0594` n `12`; crypto_alt avg `-3.7106` n `228`; crypto_major avg `-3.2479` n `8`; equity avg `-3.6809` n `73`; fx avg `-0.0657` n `6`; index avg `-1.0621` n `23`; metal avg `-1.4215` n `18`; unknown avg `-0.266` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
