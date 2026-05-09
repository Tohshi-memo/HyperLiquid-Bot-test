# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T04:37:15.186194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `0.0364` n `228`; crypto_major avg `-0.0424` n `8`; equity avg `-0.035` n `65`; fx avg `0.0` n `5`; index avg `0.0018` n `23`; metal avg `-0.0041` n `18`; unknown avg `-0.1835` n `375`
- 1h: commodity avg `0.0971` n `12`; crypto_alt avg `0.1762` n `228`; crypto_major avg `0.0813` n `8`; equity avg `-0.0067` n `65`; fx avg `0.0` n `5`; index avg `0.0636` n `23`; metal avg `-0.0332` n `18`; unknown avg `-0.1439` n `375`
- 4h: commodity avg `0.1589` n `12`; crypto_alt avg `0.7151` n `228`; crypto_major avg `0.639` n `8`; equity avg `0.042` n `65`; fx avg `-0.0064` n `5`; index avg `0.1324` n `23`; metal avg `0.2202` n `18`; unknown avg `-0.0924` n `375`
- 24h: commodity avg `-0.422` n `12`; crypto_alt avg `4.5941` n `228`; crypto_major avg `2.9975` n `8`; equity avg `3.6641` n `65`; fx avg `0.0377` n `5`; index avg `1.4446` n `23`; metal avg `0.431` n `18`; unknown avg `1.4563` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
