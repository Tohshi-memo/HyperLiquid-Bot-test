# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T08:52:32.941286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3054` n `12`; crypto_alt avg `-0.026` n `228`; crypto_major avg `-0.062` n `8`; equity avg `-0.2029` n `74`; fx avg `-0.0301` n `6`; index avg `-0.2021` n `23`; metal avg `0.0207` n `18`; unknown avg `-0.0136` n `547`
- 1h: commodity avg `-0.4102` n `12`; crypto_alt avg `-0.5452` n `228`; crypto_major avg `-0.8162` n `8`; equity avg `-0.5922` n `74`; fx avg `-0.0623` n `6`; index avg `-0.3574` n `23`; metal avg `-0.2284` n `18`; unknown avg `0.1992` n `547`
- 4h: commodity avg `-0.2005` n `12`; crypto_alt avg `0.1549` n `228`; crypto_major avg `-0.2744` n `8`; equity avg `-0.1181` n `74`; fx avg `-0.0054` n `6`; index avg `-0.2532` n `23`; metal avg `0.4176` n `18`; unknown avg `-0.1174` n `537`
- 24h: commodity avg `-0.6502` n `12`; crypto_alt avg `-1.8536` n `228`; crypto_major avg `-4.2019` n `8`; equity avg `-4.2291` n `74`; fx avg `0.0532` n `6`; index avg `-2.3276` n `23`; metal avg `-3.3022` n `18`; unknown avg `0.1961` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
