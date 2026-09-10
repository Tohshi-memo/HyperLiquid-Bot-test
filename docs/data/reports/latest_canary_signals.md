# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T21:10:37.911928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `0.1939` n `233`; crypto_major avg `0.0841` n `8`; equity avg `0.0364` n `136`; fx avg `0.0117` n `6`; index avg `0.0043` n `26`; metal avg `0.0267` n `20`; unknown avg `2.2612` n `794`
- 1h: commodity avg `0.1593` n `12`; crypto_alt avg `0.3478` n `233`; crypto_major avg `0.1726` n `8`; equity avg `0.17` n `136`; fx avg `-0.0037` n `6`; index avg `0.0114` n `26`; metal avg `0.0275` n `20`; unknown avg `10.5477` n `770`
- 4h: commodity avg `0.4249` n `12`; crypto_alt avg `0.423` n `233`; crypto_major avg `0.4956` n `8`; equity avg `-0.5374` n `136`; fx avg `0.0131` n `6`; index avg `-0.0507` n `26`; metal avg `-0.2107` n `20`; unknown avg `5.7712` n `749`
- 24h: commodity avg `1.2013` n `12`; crypto_alt avg `-2.774` n `233`; crypto_major avg `-2.215` n `8`; equity avg `-2.0582` n `136`; fx avg `0.1213` n `6`; index avg `-0.3251` n `26`; metal avg `-1.2492` n `20`; unknown avg `-1.6508` n `667`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
