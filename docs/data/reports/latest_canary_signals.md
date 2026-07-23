# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T22:42:19.386447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0208` n `12`; crypto_alt avg `0.049` n `230`; crypto_major avg `0.0565` n `8`; equity avg `0.0284` n `100`; fx avg `0.0015` n `6`; index avg `-0.0064` n `25`; metal avg `0.0225` n `20`; unknown avg `0.0667` n `772`
- 1h: commodity avg `-0.0503` n `12`; crypto_alt avg `-0.1148` n `230`; crypto_major avg `0.0617` n `8`; equity avg `-0.104` n `100`; fx avg `0.0043` n `6`; index avg `-0.0643` n `25`; metal avg `-0.0156` n `20`; unknown avg `0.0522` n `772`
- 4h: commodity avg `-0.038` n `12`; crypto_alt avg `-0.1601` n `230`; crypto_major avg `0.0194` n `8`; equity avg `0.0421` n `100`; fx avg `-0.0025` n `6`; index avg `0.0262` n `25`; metal avg `0.0486` n `20`; unknown avg `0.2132` n `772`
- 24h: commodity avg `0.6015` n `12`; crypto_alt avg `-1.5412` n `230`; crypto_major avg `-1.9376` n `8`; equity avg `-1.1837` n `99`; fx avg `-0.06` n `6`; index avg `-0.2593` n `25`; metal avg `-0.658` n `20`; unknown avg `-0.2789` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
