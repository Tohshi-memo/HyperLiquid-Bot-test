# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T08:37:29.055569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1014` n `12`; crypto_alt avg `-0.0517` n `228`; crypto_major avg `-0.1233` n `8`; equity avg `-0.2556` n `74`; fx avg `0.0143` n `6`; index avg `-0.1435` n `23`; metal avg `-0.1173` n `18`; unknown avg `0.3514` n `643`
- 1h: commodity avg `-1.0089` n `12`; crypto_alt avg `0.8049` n `228`; crypto_major avg `0.773` n `8`; equity avg `0.6082` n `74`; fx avg `-0.0177` n `6`; index avg `0.2949` n `23`; metal avg `0.8868` n `18`; unknown avg `0.2794` n `531`
- 4h: commodity avg `-1.0489` n `12`; crypto_alt avg `-0.322` n `228`; crypto_major avg `-0.4374` n `8`; equity avg `-0.4558` n `74`; fx avg `-0.0434` n `6`; index avg `-0.2625` n `23`; metal avg `0.2011` n `18`; unknown avg `-0.0615` n `515`
- 24h: commodity avg `-2.5716` n `12`; crypto_alt avg `1.021` n `228`; crypto_major avg `1.2087` n `8`; equity avg `2.2305` n `74`; fx avg `-0.0311` n `6`; index avg `1.3066` n `23`; metal avg `2.7832` n `18`; unknown avg `2.0302` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
