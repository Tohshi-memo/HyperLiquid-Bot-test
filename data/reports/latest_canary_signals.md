# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T09:22:26.071206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.5568` n `231`; crypto_major avg `-0.5359` n `8`; equity avg `-0.0375` n `122`; fx avg `-0.006` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0282` n `20`; unknown avg `-0.1414` n `797`
- 1h: commodity avg `-0.1307` n `12`; crypto_alt avg `-0.5798` n `231`; crypto_major avg `-0.6034` n `8`; equity avg `0.0381` n `122`; fx avg `-0.0076` n `6`; index avg `0.0107` n `25`; metal avg `-0.0378` n `20`; unknown avg `-0.0785` n `797`
- 4h: commodity avg `-0.1493` n `12`; crypto_alt avg `-0.3007` n `231`; crypto_major avg `-0.3461` n `8`; equity avg `-0.202` n `122`; fx avg `-0.0119` n `6`; index avg `-0.0216` n `25`; metal avg `-0.1589` n `20`; unknown avg `0.0503` n `781`
- 24h: commodity avg `-0.3712` n `12`; crypto_alt avg `-2.4757` n `231`; crypto_major avg `-2.513` n `8`; equity avg `0.1617` n `122`; fx avg `-0.0579` n `6`; index avg `-0.0272` n `25`; metal avg `0.17` n `20`; unknown avg `0.5495` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
