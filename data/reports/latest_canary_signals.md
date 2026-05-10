# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T00:37:19.881580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `-0.0959` n `228`; crypto_major avg `-0.1227` n `8`; equity avg `0.0022` n `65`; fx avg `0.0` n `5`; index avg `0.0058` n `23`; metal avg `0.0072` n `18`; unknown avg `-0.0158` n `376`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `-0.144` n `228`; crypto_major avg `-0.0572` n `8`; equity avg `0.0215` n `65`; fx avg `0.0008` n `5`; index avg `0.013` n `23`; metal avg `0.0377` n `18`; unknown avg `-0.3252` n `376`
- 4h: commodity avg `-0.055` n `12`; crypto_alt avg `-0.3354` n `228`; crypto_major avg `-0.1821` n `8`; equity avg `0.1867` n `65`; fx avg `-0.0289` n `5`; index avg `0.14` n `23`; metal avg `0.1048` n `18`; unknown avg `-0.2767` n `376`
- 24h: commodity avg `0.5018` n `12`; crypto_alt avg `-0.8212` n `228`; crypto_major avg `-0.1228` n `8`; equity avg `0.726` n `65`; fx avg `-0.0166` n `5`; index avg `0.3419` n `23`; metal avg `0.3859` n `18`; unknown avg `-0.1119` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
