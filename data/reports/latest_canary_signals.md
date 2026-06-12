# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T10:07:35.017818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `12`; crypto_alt avg `0.0835` n `228`; crypto_major avg `-0.0597` n `8`; equity avg `0.0482` n `74`; fx avg `-0.0066` n `6`; index avg `0.0431` n `23`; metal avg `-0.048` n `18`; unknown avg `-0.0178` n `643`
- 1h: commodity avg `0.1856` n `12`; crypto_alt avg `0.6331` n `228`; crypto_major avg `0.4508` n `8`; equity avg `0.4595` n `74`; fx avg `0.0187` n `6`; index avg `0.2577` n `23`; metal avg `0.2184` n `18`; unknown avg `0.2347` n `643`
- 4h: commodity avg `-0.982` n `12`; crypto_alt avg `1.2377` n `228`; crypto_major avg `0.7278` n `8`; equity avg `0.7347` n `74`; fx avg `-0.0032` n `6`; index avg `0.4106` n `23`; metal avg `0.719` n `18`; unknown avg `0.3165` n `531`
- 24h: commodity avg `-2.526` n `12`; crypto_alt avg `2.131` n `228`; crypto_major avg `2.0978` n `8`; equity avg `2.9155` n `74`; fx avg `0.0117` n `6`; index avg `1.5943` n `23`; metal avg `3.4044` n `18`; unknown avg `-0.5397` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
