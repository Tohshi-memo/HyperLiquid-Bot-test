# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T06:22:33.463147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1025` n `12`; crypto_alt avg `-0.0678` n `228`; crypto_major avg `0.0841` n `8`; equity avg `0.0544` n `86`; fx avg `0.0104` n `6`; index avg `0.0179` n `23`; metal avg `-0.0505` n `20`; unknown avg `0.0372` n `764`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.0231` n `228`; crypto_major avg `0.1706` n `8`; equity avg `0.0766` n `86`; fx avg `0.0157` n `6`; index avg `-0.0076` n `23`; metal avg `0.2658` n `20`; unknown avg `0.2126` n `748`
- 4h: commodity avg `-0.0403` n `12`; crypto_alt avg `-0.199` n `228`; crypto_major avg `0.1857` n `8`; equity avg `0.0918` n `86`; fx avg `0.05` n `6`; index avg `0.0088` n `23`; metal avg `0.2596` n `20`; unknown avg `-0.068` n `740`
- 24h: commodity avg `-0.3382` n `12`; crypto_alt avg `0.0684` n `228`; crypto_major avg `-0.4457` n `8`; equity avg `5.1237` n `86`; fx avg `-0.1203` n `6`; index avg `0.0632` n `23`; metal avg `-0.2295` n `20`; unknown avg `0.0094` n `580`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
