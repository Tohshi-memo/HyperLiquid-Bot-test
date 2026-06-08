# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T15:37:27.417270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0727` n `12`; crypto_alt avg `-0.2645` n `228`; crypto_major avg `-0.261` n `8`; equity avg `-0.2786` n `74`; fx avg `-0.0093` n `6`; index avg `-0.1072` n `23`; metal avg `-0.2121` n `18`; unknown avg `0.0745` n `517`
- 1h: commodity avg `-0.1588` n `12`; crypto_alt avg `0.4834` n `228`; crypto_major avg `0.5311` n `8`; equity avg `0.2069` n `74`; fx avg `0.0173` n `6`; index avg `0.2288` n `23`; metal avg `0.4351` n `18`; unknown avg `-0.0467` n `517`
- 4h: commodity avg `-0.0201` n `12`; crypto_alt avg `0.3171` n `228`; crypto_major avg `0.7764` n `8`; equity avg `0.69` n `74`; fx avg `-0.0107` n `6`; index avg `0.3459` n `23`; metal avg `-0.1736` n `18`; unknown avg `-2.081` n `517`
- 24h: commodity avg `-0.4845` n `12`; crypto_alt avg `2.1771` n `228`; crypto_major avg `3.5826` n `8`; equity avg `2.4191` n `74`; fx avg `-0.2698` n `6`; index avg `1.1561` n `23`; metal avg `0.0261` n `18`; unknown avg `-3.1064` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
