# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T03:07:15.048322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.0647` n `228`; crypto_major avg `0.0014` n `8`; equity avg `0.0235` n `65`; fx avg `0.0` n `5`; index avg `-0.0461` n `23`; metal avg `0.0072` n `18`; unknown avg `-0.4088` n `375`
- 1h: commodity avg `0.1022` n `12`; crypto_alt avg `0.0754` n `228`; crypto_major avg `-0.0851` n `8`; equity avg `0.0595` n `65`; fx avg `-0.0189` n `5`; index avg `-0.0059` n `23`; metal avg `0.1099` n `18`; unknown avg `-0.4094` n `375`
- 4h: commodity avg `0.0133` n `12`; crypto_alt avg `1.2136` n `228`; crypto_major avg `0.7888` n `8`; equity avg `0.2046` n `65`; fx avg `-0.0136` n `5`; index avg `0.0898` n `23`; metal avg `0.2723` n `18`; unknown avg `0.2083` n `375`
- 24h: commodity avg `-0.2647` n `12`; crypto_alt avg `5.2842` n `228`; crypto_major avg `3.0473` n `8`; equity avg `3.8726` n `65`; fx avg `0.0937` n `5`; index avg `1.4137` n `23`; metal avg `0.4777` n `18`; unknown avg `1.3247` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
