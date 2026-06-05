# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T02:07:21.078125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0849` n `12`; crypto_alt avg `-0.2746` n `228`; crypto_major avg `-0.2206` n `8`; equity avg `0.0425` n `74`; fx avg `-0.0086` n `6`; index avg `0.0639` n `23`; metal avg `-0.0713` n `18`; unknown avg `-0.258` n `424`
- 1h: commodity avg `0.3028` n `12`; crypto_alt avg `0.2472` n `228`; crypto_major avg `0.2976` n `8`; equity avg `0.6594` n `74`; fx avg `0.0516` n `6`; index avg `0.134` n `23`; metal avg `-0.3587` n `18`; unknown avg `-0.069` n `424`
- 4h: commodity avg `0.1219` n `12`; crypto_alt avg `0.3092` n `228`; crypto_major avg `0.3255` n `8`; equity avg `-0.7553` n `74`; fx avg `0.1542` n `6`; index avg `-0.6576` n `23`; metal avg `-0.9684` n `18`; unknown avg `-0.1436` n `424`
- 24h: commodity avg `-0.0797` n `12`; crypto_alt avg `-1.582` n `228`; crypto_major avg `-0.9782` n `8`; equity avg `-0.4918` n `73`; fx avg `0.2124` n `6`; index avg `-0.2337` n `23`; metal avg `-0.43` n `18`; unknown avg `-0.3071` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
