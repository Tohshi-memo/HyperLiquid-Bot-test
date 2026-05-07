# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T19:52:10.701679+00:00`
- Correlation status: `ready`
- Asset price records: `579`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2122` n `12`; crypto_alt avg `-0.0185` n `228`; crypto_major avg `-0.081` n `8`; equity avg `0.0359` n `65`; fx avg `0.0097` n `5`; index avg `0.0002` n `23`; metal avg `-0.1026` n `18`; unknown avg `0.2147` n `365`
- 1h: commodity avg `0.1991` n `12`; crypto_alt avg `0.1678` n `228`; crypto_major avg `0.0119` n `8`; equity avg `0.1711` n `65`; fx avg `-0.0001` n `5`; index avg `0.2083` n `23`; metal avg `0.1611` n `18`; unknown avg `-0.392` n `365`
- 4h: commodity avg `1.2307` n `12`; crypto_alt avg `1.1785` n `228`; crypto_major avg `-0.0594` n `8`; equity avg `-1.0898` n `65`; fx avg `0.0151` n `5`; index avg `-0.6254` n `23`; metal avg `-0.8708` n `18`; unknown avg `-0.3167` n `365`
- 24h: commodity avg `0.8407` n `12`; crypto_alt avg `1.5122` n `228`; crypto_major avg `-1.9492` n `8`; equity avg `-1.414` n `65`; fx avg `0.1897` n `5`; index avg `-0.8644` n `23`; metal avg `0.0572` n `18`; unknown avg `-0.2804` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `575`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `575`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `575`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `575`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `571`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `571`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0936`, n `571`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.089`, n `571`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0842`, n `571`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0819`, n `571`, weak_sample_signal
