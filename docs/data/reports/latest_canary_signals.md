# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T21:22:28.114466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0503` n `12`; crypto_alt avg `-0.2539` n `233`; crypto_major avg `-0.1728` n `8`; equity avg `-0.0451` n `136`; fx avg `-0.0117` n `6`; index avg `-0.0033` n `26`; metal avg `0.0103` n `20`; unknown avg `0.3211` n `796`
- 1h: commodity avg `0.0763` n `12`; crypto_alt avg `-0.2248` n `233`; crypto_major avg `-0.2348` n `8`; equity avg `-0.0646` n `136`; fx avg `-0.0045` n `6`; index avg `-0.0064` n `26`; metal avg `0.0567` n `20`; unknown avg `18.2564` n `770`
- 4h: commodity avg `0.3487` n `12`; crypto_alt avg `0.0543` n `233`; crypto_major avg `0.124` n `8`; equity avg `-0.5271` n `136`; fx avg `0.0086` n `6`; index avg `-0.0426` n `26`; metal avg `-0.1963` n `20`; unknown avg `5.8303` n `750`
- 24h: commodity avg `1.1514` n `12`; crypto_alt avg `-2.7792` n `233`; crypto_major avg `-2.1473` n `8`; equity avg `-2.0199` n `136`; fx avg `0.1008` n `6`; index avg `-0.3241` n `26`; metal avg `-1.2309` n `20`; unknown avg `-1.6623` n `667`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
