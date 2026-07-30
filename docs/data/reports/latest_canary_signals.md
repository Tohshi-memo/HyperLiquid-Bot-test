# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T13:37:25.744740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.9631` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0406` n `12`; crypto_alt avg `-0.0763` n `230`; crypto_major avg `-0.0801` n `8`; equity avg `0.5188` n `102`; fx avg `-0.2154` n `6`; index avg `0.0403` n `25`; metal avg `0.0766` n `20`; unknown avg `0.0278` n `779`
- 1h: commodity avg `-0.0599` n `12`; crypto_alt avg `-0.2305` n `230`; crypto_major avg `-0.2826` n `8`; equity avg `1.0357` n `102`; fx avg `-0.2509` n `6`; index avg `0.1383` n `25`; metal avg `0.0859` n `20`; unknown avg `0.0075` n `779`
- 4h: commodity avg `-0.2166` n `12`; crypto_alt avg `-0.2063` n `230`; crypto_major avg `-0.1403` n `8`; equity avg `2.8228` n `102`; fx avg `-0.2922` n `6`; index avg `0.377` n `25`; metal avg `0.1514` n `20`; unknown avg `0.1011` n `779`
- 24h: commodity avg `-0.1255` n `12`; crypto_alt avg `-0.0927` n `230`; crypto_major avg `0.1266` n `8`; equity avg `0.127` n `102`; fx avg `-0.2906` n `6`; index avg `-0.0373` n `25`; metal avg `0.6342` n `20`; unknown avg `-0.2733` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
