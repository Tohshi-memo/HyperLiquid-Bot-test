# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T04:22:22.197157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `-0.2695` n `228`; crypto_major avg `-0.2411` n `8`; equity avg `-0.0739` n `74`; fx avg `-0.0099` n `6`; index avg `-0.0694` n `23`; metal avg `-0.0159` n `18`; unknown avg `-0.0489` n `517`
- 1h: commodity avg `0.021` n `12`; crypto_alt avg `-0.6985` n `228`; crypto_major avg `-1.0396` n `8`; equity avg `-0.2613` n `74`; fx avg `-0.0094` n `6`; index avg `-0.2019` n `23`; metal avg `0.1676` n `18`; unknown avg `1.5088` n `517`
- 4h: commodity avg `0.3615` n `12`; crypto_alt avg `-0.6359` n `228`; crypto_major avg `-0.5837` n `8`; equity avg `-0.1677` n `74`; fx avg `-0.053` n `6`; index avg `-0.1173` n `23`; metal avg `-0.5836` n `18`; unknown avg `-0.524` n `517`
- 24h: commodity avg `0.4223` n `12`; crypto_alt avg `0.9818` n `228`; crypto_major avg `2.997` n `8`; equity avg `1.4306` n `74`; fx avg `-0.1089` n `6`; index avg `0.1827` n `23`; metal avg `-0.1328` n `18`; unknown avg `-5.4953` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
