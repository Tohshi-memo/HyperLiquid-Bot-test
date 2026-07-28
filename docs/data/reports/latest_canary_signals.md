# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T22:37:26.490429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2153` n `12`; crypto_alt avg `-0.1349` n `230`; crypto_major avg `-0.2291` n `8`; equity avg `-0.1211` n `102`; fx avg `0.0` n `6`; index avg `-0.018` n `25`; metal avg `-0.043` n `20`; unknown avg `0.0663` n `776`
- 1h: commodity avg `0.544` n `12`; crypto_alt avg `-0.21` n `230`; crypto_major avg `-0.2189` n `8`; equity avg `-0.2219` n `102`; fx avg `-0.0062` n `6`; index avg `-0.0442` n `25`; metal avg `-0.1023` n `20`; unknown avg `0.0436` n `776`
- 4h: commodity avg `0.6465` n `12`; crypto_alt avg `0.1291` n `230`; crypto_major avg `0.2271` n `8`; equity avg `0.8702` n `102`; fx avg `0.0101` n `6`; index avg `0.0141` n `25`; metal avg `-0.0883` n `20`; unknown avg `0.2881` n `775`
- 24h: commodity avg `-0.1769` n `12`; crypto_alt avg `-1.4889` n `230`; crypto_major avg `-0.9266` n `8`; equity avg `-2.5758` n `102`; fx avg `-0.0867` n `6`; index avg `-0.3636` n `25`; metal avg `-0.4945` n `20`; unknown avg `0.1968` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
