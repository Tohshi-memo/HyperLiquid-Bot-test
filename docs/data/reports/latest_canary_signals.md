# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T20:38:06.139147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0673` n `12`; crypto_alt avg `-0.1395` n `233`; crypto_major avg `-0.125` n `8`; equity avg `-0.0466` n `136`; fx avg `0.0117` n `6`; index avg `-0.0065` n `26`; metal avg `0.0135` n `20`; unknown avg `12.9193` n `776`
- 1h: commodity avg `0.1369` n `12`; crypto_alt avg `0.1628` n `233`; crypto_major avg `0.1596` n `8`; equity avg `-0.0953` n `136`; fx avg `0.0098` n `6`; index avg `0.0133` n `26`; metal avg `-0.0255` n `20`; unknown avg `12.8414` n `754`
- 4h: commodity avg `0.3419` n `12`; crypto_alt avg `0.9944` n `233`; crypto_major avg `0.9079` n `8`; equity avg `-0.2595` n `136`; fx avg `0.0123` n `6`; index avg `-0.0118` n `26`; metal avg `-0.2257` n `20`; unknown avg `2.8644` n `753`
- 24h: commodity avg `1.1752` n `12`; crypto_alt avg `-3.1234` n `233`; crypto_major avg `-2.3292` n `8`; equity avg `-2.1116` n `136`; fx avg `0.1218` n `6`; index avg `-0.3234` n `26`; metal avg `-1.2605` n `20`; unknown avg `433.9033` n `677`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
