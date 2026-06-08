# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T07:02:36.134992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1412` n `12`; crypto_alt avg `-0.2672` n `228`; crypto_major avg `-0.1818` n `8`; equity avg `0.0766` n `74`; fx avg `-0.0489` n `6`; index avg `-0.0245` n `23`; metal avg `-0.2219` n `18`; unknown avg `-0.0822` n `517`
- 1h: commodity avg `-0.0233` n `12`; crypto_alt avg `0.0424` n `228`; crypto_major avg `0.115` n `8`; equity avg `0.1503` n `74`; fx avg `-0.1016` n `6`; index avg `0.1741` n `23`; metal avg `0.0175` n `18`; unknown avg `-0.074` n `517`
- 4h: commodity avg `0.2787` n `12`; crypto_alt avg `-0.3854` n `228`; crypto_major avg `-0.4783` n `8`; equity avg `-1.0061` n `74`; fx avg `-0.2379` n `6`; index avg `-0.3682` n `23`; metal avg `-0.3386` n `18`; unknown avg `-0.275` n `507`
- 24h: commodity avg `0.9157` n `12`; crypto_alt avg `-0.257` n `228`; crypto_major avg `1.6083` n `8`; equity avg `0.1446` n `74`; fx avg `-0.3256` n `6`; index avg `-0.0494` n `23`; metal avg `-0.8621` n `18`; unknown avg `-5.5935` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
