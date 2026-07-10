# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T03:37:24.204082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0236` n `12`; crypto_alt avg `0.0462` n `229`; crypto_major avg `0.1168` n `8`; equity avg `-0.1227` n `91`; fx avg `0.0098` n `6`; index avg `-0.0248` n `25`; metal avg `-0.0131` n `20`; unknown avg `0.0564` n `765`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `0.0345` n `229`; crypto_major avg `0.0753` n `8`; equity avg `-0.0102` n `91`; fx avg `0.0095` n `6`; index avg `0.0304` n `25`; metal avg `0.0725` n `20`; unknown avg `4.6681` n `765`
- 4h: commodity avg `0.1001` n `12`; crypto_alt avg `0.9142` n `229`; crypto_major avg `1.2006` n `8`; equity avg `-0.0133` n `91`; fx avg `0.0053` n `6`; index avg `-0.017` n `25`; metal avg `0.2032` n `20`; unknown avg `0.7656` n `763`
- 24h: commodity avg `-0.9792` n `12`; crypto_alt avg `1.7847` n `229`; crypto_major avg `1.787` n `8`; equity avg `1.78` n `91`; fx avg `0.0394` n `6`; index avg `0.4276` n `25`; metal avg `0.9756` n `20`; unknown avg `0.1662` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
