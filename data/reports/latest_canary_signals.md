# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T06:37:26.793049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `0.0431` n `233`; crypto_major avg `-0.0658` n `8`; equity avg `-0.0448` n `136`; fx avg `-0.0046` n `6`; index avg `-0.0144` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.0127` n `838`
- 1h: commodity avg `0.0308` n `12`; crypto_alt avg `-0.0355` n `233`; crypto_major avg `-0.2075` n `8`; equity avg `-0.1337` n `136`; fx avg `-0.0053` n `6`; index avg `-0.0297` n `26`; metal avg `0.0012` n `20`; unknown avg `-0.0321` n `812`
- 4h: commodity avg `0.0867` n `12`; crypto_alt avg `0.1695` n `233`; crypto_major avg `-0.2649` n `8`; equity avg `-0.3404` n `136`; fx avg `-0.0092` n `6`; index avg `-0.0743` n `26`; metal avg `0.0051` n `20`; unknown avg `-0.0667` n `804`
- 24h: commodity avg `0.1658` n `12`; crypto_alt avg `0.8671` n `233`; crypto_major avg `-0.0667` n `8`; equity avg `-0.6866` n `136`; fx avg `-0.0112` n `6`; index avg `-0.1209` n `26`; metal avg `0.0315` n `20`; unknown avg `0.4819` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
