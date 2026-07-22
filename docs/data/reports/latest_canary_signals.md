# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T14:22:33.769621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.3337` n `230`; crypto_major avg `-0.5331` n `8`; equity avg `-0.1236` n `98`; fx avg `-0.0027` n `6`; index avg `0.0231` n `25`; metal avg `-0.0838` n `20`; unknown avg `0.0962` n `773`
- 1h: commodity avg `0.1315` n `12`; crypto_alt avg `0.2304` n `230`; crypto_major avg `0.2731` n `8`; equity avg `1.0469` n `98`; fx avg `-0.0202` n `6`; index avg `0.1788` n `25`; metal avg `0.1466` n `20`; unknown avg `10.5504` n `773`
- 4h: commodity avg `0.1056` n `12`; crypto_alt avg `0.1522` n `230`; crypto_major avg `-0.0892` n `8`; equity avg `0.6205` n `98`; fx avg `-0.0229` n `6`; index avg `0.1045` n `25`; metal avg `0.1505` n `20`; unknown avg `11.2575` n `773`
- 24h: commodity avg `0.5197` n `12`; crypto_alt avg `-0.36` n `230`; crypto_major avg `-1.2476` n `8`; equity avg `0.8084` n `98`; fx avg `-0.0338` n `6`; index avg `0.0731` n `25`; metal avg `0.5752` n `20`; unknown avg `0.8885` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1036`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0684`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0628`, n `666`, weak_sample_signal
