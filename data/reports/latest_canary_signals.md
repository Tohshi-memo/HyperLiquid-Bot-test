# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T18:07:31.253929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0446` n `12`; crypto_alt avg `0.1327` n `228`; crypto_major avg `0.2542` n `8`; equity avg `0.1046` n `85`; fx avg `0.0057` n `6`; index avg `0.0035` n `23`; metal avg `0.032` n `20`; unknown avg `-0.0901` n `717`
- 1h: commodity avg `-0.0513` n `12`; crypto_alt avg `-0.0242` n `228`; crypto_major avg `0.2975` n `8`; equity avg `0.3879` n `85`; fx avg `-0.0068` n `6`; index avg `0.025` n `23`; metal avg `-0.0488` n `20`; unknown avg `0.0732` n `717`
- 4h: commodity avg `-0.0265` n `12`; crypto_alt avg `-1.0661` n `228`; crypto_major avg `-0.9732` n `8`; equity avg `-1.202` n `85`; fx avg `-0.0431` n `6`; index avg `-0.1086` n `23`; metal avg `-0.364` n `20`; unknown avg `0.0157` n `716`
- 24h: commodity avg `-0.8994` n `12`; crypto_alt avg `-0.01` n `228`; crypto_major avg `0.4464` n `8`; equity avg `-0.3321` n `85`; fx avg `0.0334` n `6`; index avg `0.1529` n `23`; metal avg `0.2469` n `18`; unknown avg `1.007` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
