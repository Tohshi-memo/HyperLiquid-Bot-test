# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T14:07:29.920945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0769` n `12`; crypto_alt avg `-0.0364` n `228`; crypto_major avg `-0.2458` n `8`; equity avg `0.1343` n `74`; fx avg `-0.02` n `6`; index avg `0.1294` n `23`; metal avg `-0.1459` n `18`; unknown avg `-0.0822` n `556`
- 1h: commodity avg `-0.6481` n `12`; crypto_alt avg `0.4378` n `228`; crypto_major avg `0.2935` n `8`; equity avg `0.8186` n `74`; fx avg `-0.0356` n `6`; index avg `0.4065` n `23`; metal avg `0.4282` n `18`; unknown avg `0.1121` n `556`
- 4h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.0396` n `228`; crypto_major avg `0.1018` n `8`; equity avg `0.2717` n `74`; fx avg `-0.0314` n `6`; index avg `0.1822` n `23`; metal avg `0.1976` n `18`; unknown avg `-1.436` n `556`
- 24h: commodity avg `-0.7477` n `12`; crypto_alt avg `0.2576` n `228`; crypto_major avg `0.028` n `8`; equity avg `-0.6945` n `74`; fx avg `-0.0288` n `6`; index avg `-0.3806` n `23`; metal avg `-1.2164` n `18`; unknown avg `2.3991` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
