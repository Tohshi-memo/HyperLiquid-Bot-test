# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T01:22:27.286958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `-0.2956` n `233`; crypto_major avg `-0.2561` n `8`; equity avg `-0.1757` n `136`; fx avg `0.0155` n `6`; index avg `-0.0347` n `26`; metal avg `-0.0682` n `20`; unknown avg `-0.0731` n `796`
- 1h: commodity avg `-0.0728` n `12`; crypto_alt avg `-0.0548` n `233`; crypto_major avg `0.0556` n `8`; equity avg `0.1307` n `136`; fx avg `-0.0056` n `6`; index avg `0.0283` n `26`; metal avg `0.0106` n `20`; unknown avg `0.995` n `788`
- 4h: commodity avg `-0.2002` n `12`; crypto_alt avg `-0.7384` n `233`; crypto_major avg `-0.674` n `8`; equity avg `-0.1001` n `136`; fx avg `0.0023` n `6`; index avg `0.0131` n `26`; metal avg `-0.0238` n `20`; unknown avg `0.3146` n `750`
- 24h: commodity avg `0.9974` n `12`; crypto_alt avg `-1.8321` n `233`; crypto_major avg `-2.0041` n `8`; equity avg `-1.5968` n `136`; fx avg `0.104` n `6`; index avg `-0.2409` n `26`; metal avg `-1.2673` n `20`; unknown avg `-0.4539` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
