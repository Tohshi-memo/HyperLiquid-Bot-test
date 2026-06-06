# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T07:07:21.567859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0535` n `12`; crypto_alt avg `0.1097` n `228`; crypto_major avg `0.0665` n `8`; equity avg `-0.0963` n `74`; fx avg `-0.004` n `6`; index avg `-0.0955` n `23`; metal avg `0.024` n `18`; unknown avg `0.0107` n `425`
- 1h: commodity avg `-0.1918` n `12`; crypto_alt avg `-0.228` n `228`; crypto_major avg `-0.2385` n `8`; equity avg `-0.2246` n `74`; fx avg `-0.0138` n `6`; index avg `-0.0866` n `23`; metal avg `0.0894` n `18`; unknown avg `1.1589` n `425`
- 4h: commodity avg `-0.4236` n `12`; crypto_alt avg `-0.8244` n `228`; crypto_major avg `-0.3056` n `8`; equity avg `0.1484` n `74`; fx avg `-0.0162` n `6`; index avg `-0.0765` n `23`; metal avg `-0.011` n `18`; unknown avg `-0.3684` n `415`
- 24h: commodity avg `-1.3375` n `12`; crypto_alt avg `-2.6115` n `228`; crypto_major avg `-1.7368` n `8`; equity avg `-6.0295` n `74`; fx avg `-0.2051` n `6`; index avg `-4.0101` n `23`; metal avg `-4.1053` n `18`; unknown avg `1.9606` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
