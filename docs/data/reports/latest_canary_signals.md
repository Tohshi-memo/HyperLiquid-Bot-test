# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T03:22:29.023442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `12`; crypto_alt avg `-0.1952` n `228`; crypto_major avg `-0.2299` n `8`; equity avg `-0.1134` n `74`; fx avg `-0.0129` n `6`; index avg `-0.066` n `23`; metal avg `0.1123` n `18`; unknown avg `0.357` n `557`
- 1h: commodity avg `0.2356` n `12`; crypto_alt avg `-0.1224` n `228`; crypto_major avg `-0.1532` n `8`; equity avg `-0.0681` n `74`; fx avg `0.008` n `6`; index avg `-0.1244` n `23`; metal avg `0.1873` n `18`; unknown avg `0.0079` n `557`
- 4h: commodity avg `0.4159` n `12`; crypto_alt avg `0.1927` n `228`; crypto_major avg `-0.0121` n `8`; equity avg `0.1487` n `74`; fx avg `0.0075` n `6`; index avg `-0.2577` n `23`; metal avg `0.0695` n `18`; unknown avg `-0.1379` n `556`
- 24h: commodity avg `-2.2054` n `12`; crypto_alt avg `3.1196` n `228`; crypto_major avg `3.1474` n `8`; equity avg `4.3106` n `74`; fx avg `0.0193` n `6`; index avg `2.1358` n `23`; metal avg `3.8224` n `18`; unknown avg `2.3716` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
