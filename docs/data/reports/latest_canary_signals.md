# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T21:07:27.196292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `-0.0277` n `234`; crypto_major avg `0.0845` n `8`; equity avg `-0.0112` n `140`; fx avg `0.0037` n `6`; index avg `0.0082` n `26`; metal avg `-0.011` n `20`; unknown avg `-0.0709` n `942`
- 1h: commodity avg `0.049` n `12`; crypto_alt avg `0.2816` n `234`; crypto_major avg `0.0227` n `8`; equity avg `0.0123` n `140`; fx avg `-0.0095` n `6`; index avg `-0.0108` n `26`; metal avg `-0.0284` n `20`; unknown avg `0.2148` n `912`
- 4h: commodity avg `-0.0923` n `12`; crypto_alt avg `0.6669` n `234`; crypto_major avg `0.2225` n `8`; equity avg `0.2841` n `140`; fx avg `-0.0118` n `6`; index avg `0.046` n `26`; metal avg `0.2278` n `20`; unknown avg `0.6332` n `906`
- 24h: commodity avg `0.1541` n `12`; crypto_alt avg `2.3541` n `234`; crypto_major avg `0.4777` n `8`; equity avg `0.9105` n `140`; fx avg `-0.299` n `6`; index avg `0.1097` n `26`; metal avg `0.2663` n `20`; unknown avg `1.0588` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
