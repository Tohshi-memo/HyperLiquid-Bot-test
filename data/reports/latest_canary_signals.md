# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T16:37:34.898896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.3417` n `228`; crypto_major avg `0.2307` n `8`; equity avg `0.2157` n `74`; fx avg `0.0018` n `6`; index avg `0.0506` n `23`; metal avg `-0.207` n `18`; unknown avg `-0.1448` n `556`
- 1h: commodity avg `0.2727` n `12`; crypto_alt avg `0.0884` n `228`; crypto_major avg `-0.2409` n `8`; equity avg `0.1304` n `74`; fx avg `-0.0156` n `6`; index avg `0.0547` n `23`; metal avg `0.0066` n `18`; unknown avg `-0.3533` n `556`
- 4h: commodity avg `-0.1865` n `12`; crypto_alt avg `0.7543` n `228`; crypto_major avg `0.3585` n `8`; equity avg `0.9388` n `74`; fx avg `-0.073` n `6`; index avg `0.4596` n `23`; metal avg `0.7428` n `18`; unknown avg `0.1151` n `556`
- 24h: commodity avg `-0.5369` n `12`; crypto_alt avg `0.7155` n `228`; crypto_major avg `0.3636` n `8`; equity avg `0.0184` n `74`; fx avg `-0.062` n `6`; index avg `0.0729` n `23`; metal avg `-0.7839` n `18`; unknown avg `2.0396` n `528`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
