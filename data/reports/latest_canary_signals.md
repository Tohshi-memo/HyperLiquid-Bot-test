# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T10:22:29.440515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.55` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.0396` n `233`; crypto_major avg `-0.0276` n `8`; equity avg `0.0041` n `136`; fx avg `-0.0014` n `6`; index avg `0.0019` n `26`; metal avg `0.0038` n `20`; unknown avg `-0.0306` n `838`
- 1h: commodity avg `0.0638` n `12`; crypto_alt avg `0.1269` n `233`; crypto_major avg `0.158` n `8`; equity avg `0.0148` n `136`; fx avg `-0.0025` n `6`; index avg `0.0034` n `26`; metal avg `0.0077` n `20`; unknown avg `0.1711` n `836`
- 4h: commodity avg `0.0801` n `12`; crypto_alt avg `0.5041` n `233`; crypto_major avg `0.5876` n `8`; equity avg `0.0154` n `136`; fx avg `0.0` n `6`; index avg `0.0044` n `26`; metal avg `0.0091` n `20`; unknown avg `0.5354` n `830`
- 24h: commodity avg `0.0466` n `12`; crypto_alt avg `2.1794` n `233`; crypto_major avg `1.6066` n `8`; equity avg `0.0545` n `136`; fx avg `-0.0638` n `6`; index avg `0.1051` n `26`; metal avg `-0.0755` n `20`; unknown avg `0.9978` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
