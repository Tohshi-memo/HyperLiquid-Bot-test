# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T14:22:31.619910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3769` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0468` n `12`; crypto_alt avg `0.0001` n `228`; crypto_major avg `0.1157` n `8`; equity avg `-0.1451` n `74`; fx avg `-0.013` n `6`; index avg `-0.1261` n `23`; metal avg `0.0106` n `18`; unknown avg `-0.0877` n `517`
- 1h: commodity avg `0.0757` n `12`; crypto_alt avg `-0.413` n `228`; crypto_major avg `-0.2279` n `8`; equity avg `-0.6854` n `74`; fx avg `-0.0085` n `6`; index avg `-0.2214` n `23`; metal avg `-0.5939` n `18`; unknown avg `0.0149` n `517`
- 4h: commodity avg `-1.0203` n `12`; crypto_alt avg `1.1553` n `228`; crypto_major avg `1.3566` n `8`; equity avg `0.9398` n `74`; fx avg `0.0275` n `6`; index avg `0.4852` n `23`; metal avg `0.3543` n `18`; unknown avg `-1.4975` n `517`
- 24h: commodity avg `-0.4179` n `12`; crypto_alt avg `1.7657` n `228`; crypto_major avg `3.2388` n `8`; equity avg `1.4553` n `74`; fx avg `-0.2774` n `6`; index avg `0.6917` n `23`; metal avg `-0.429` n `18`; unknown avg `-2.8991` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
