# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T01:52:27.279141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.0995` n `233`; crypto_major avg `0.0401` n `8`; equity avg `0.0053` n `136`; fx avg `-0.0011` n `6`; index avg `-0.0133` n `26`; metal avg `-0.0105` n `20`; unknown avg `-0.0479` n `838`
- 1h: commodity avg `-0.0582` n `12`; crypto_alt avg `0.2463` n `233`; crypto_major avg `0.1773` n `8`; equity avg `0.0303` n `136`; fx avg `0.0168` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0263` n `20`; unknown avg `8.4453` n `832`
- 4h: commodity avg `-0.0953` n `12`; crypto_alt avg `0.8572` n `233`; crypto_major avg `-0.1125` n `8`; equity avg `0.1233` n `136`; fx avg `-0.0014` n `6`; index avg `0.017` n `26`; metal avg `-0.0675` n `20`; unknown avg `4.8634` n `820`
- 24h: commodity avg `-0.6693` n `12`; crypto_alt avg `1.3705` n `233`; crypto_major avg `1.2941` n `8`; equity avg `0.8813` n `136`; fx avg `-0.1699` n `6`; index avg `0.3234` n `26`; metal avg `0.2284` n `20`; unknown avg `29.6171` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
