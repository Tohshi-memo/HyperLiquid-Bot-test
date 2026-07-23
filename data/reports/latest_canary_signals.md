# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T00:22:31.200894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `0.1112` n `230`; crypto_major avg `0.101` n `8`; equity avg `0.1137` n `98`; fx avg `-0.0097` n `6`; index avg `0.0312` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.2147` n `773`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `0.4308` n `230`; crypto_major avg `0.535` n `8`; equity avg `0.5835` n `98`; fx avg `0.0037` n `6`; index avg `0.1578` n `25`; metal avg `0.0939` n `20`; unknown avg `-0.1832` n `773`
- 4h: commodity avg `0.26` n `12`; crypto_alt avg `0.0793` n `230`; crypto_major avg `0.3836` n `8`; equity avg `0.1473` n `98`; fx avg `-0.0126` n `6`; index avg `0.0339` n `25`; metal avg `-0.0568` n `20`; unknown avg `-0.1139` n `773`
- 24h: commodity avg `0.714` n `12`; crypto_alt avg `-0.5839` n `230`; crypto_major avg `-0.6107` n `8`; equity avg `-1.0734` n `98`; fx avg `-0.0416` n `6`; index avg `-0.1245` n `25`; metal avg `0.1312` n `20`; unknown avg `1.6121` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0688`, n `666`, weak_sample_signal
