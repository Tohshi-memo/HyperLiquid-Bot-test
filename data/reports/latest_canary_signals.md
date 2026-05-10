# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T08:22:18.748719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.217` n `228`; crypto_major avg `0.0926` n `8`; equity avg `-0.0094` n `65`; fx avg `0.0013` n `5`; index avg `-0.0063` n `23`; metal avg `0.0118` n `18`; unknown avg `0.1474` n `376`
- 1h: commodity avg `-0.0881` n `12`; crypto_alt avg `0.2141` n `228`; crypto_major avg `0.0777` n `8`; equity avg `0.0084` n `65`; fx avg `0.003` n `5`; index avg `-0.005` n `23`; metal avg `-0.0195` n `18`; unknown avg `-0.1001` n `376`
- 4h: commodity avg `-0.0747` n `12`; crypto_alt avg `0.6485` n `228`; crypto_major avg `0.2473` n `8`; equity avg `0.0267` n `65`; fx avg `0.0053` n `5`; index avg `-0.0055` n `23`; metal avg `0.0018` n `18`; unknown avg `0.0951` n `366`
- 24h: commodity avg `0.1189` n `12`; crypto_alt avg `-0.7843` n `228`; crypto_major avg `-0.3748` n `8`; equity avg `0.8772` n `65`; fx avg `-0.0218` n `5`; index avg `0.2549` n `23`; metal avg `0.3337` n `18`; unknown avg `-0.1616` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
