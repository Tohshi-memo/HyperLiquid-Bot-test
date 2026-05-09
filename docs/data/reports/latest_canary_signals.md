# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T11:07:21.033845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `12`; crypto_alt avg `0.1116` n `228`; crypto_major avg `0.059` n `8`; equity avg `0.032` n `65`; fx avg `0.0023` n `5`; index avg `-0.0062` n `23`; metal avg `-0.0042` n `18`; unknown avg `-0.4317` n `376`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `0.4948` n `228`; crypto_major avg `0.1397` n `8`; equity avg `0.0353` n `65`; fx avg `0.0072` n `5`; index avg `-0.0169` n `23`; metal avg `-0.0246` n `18`; unknown avg `-0.3047` n `376`
- 4h: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.3527` n `228`; crypto_major avg `-0.2033` n `8`; equity avg `0.078` n `65`; fx avg `0.0081` n `5`; index avg `-0.0061` n `23`; metal avg `-0.0473` n `18`; unknown avg `-0.6096` n `376`
- 24h: commodity avg `-0.0526` n `12`; crypto_alt avg `3.3015` n `228`; crypto_major avg `1.9397` n `8`; equity avg `2.843` n `65`; fx avg `-0.0124` n `5`; index avg `1.1338` n `23`; metal avg `-0.319` n `18`; unknown avg `0.4116` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
