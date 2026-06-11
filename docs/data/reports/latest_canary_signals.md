# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T04:07:32.739071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0548` n `12`; crypto_alt avg `0.6946` n `228`; crypto_major avg `0.2545` n `8`; equity avg `0.1259` n `74`; fx avg `-0.005` n `6`; index avg `0.0666` n `23`; metal avg `0.1177` n `18`; unknown avg `4.1731` n `550`
- 1h: commodity avg `0.1505` n `12`; crypto_alt avg `1.1993` n `228`; crypto_major avg `0.7145` n `8`; equity avg `0.4804` n `74`; fx avg `-0.0082` n `6`; index avg `0.186` n `23`; metal avg `0.1835` n `18`; unknown avg `3.2351` n `550`
- 4h: commodity avg `-0.1499` n `12`; crypto_alt avg `2.0699` n `228`; crypto_major avg `1.7082` n `8`; equity avg `1.3526` n `74`; fx avg `0.0531` n `6`; index avg `0.495` n `23`; metal avg `1.0584` n `18`; unknown avg `2.1024` n `550`
- 24h: commodity avg `1.5708` n `12`; crypto_alt avg `0.8762` n `228`; crypto_major avg `0.4592` n `8`; equity avg `-0.4524` n `74`; fx avg `0.016` n `6`; index avg `-0.8221` n `23`; metal avg `-0.6802` n `18`; unknown avg `2.744` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
