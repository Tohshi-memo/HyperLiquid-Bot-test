# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T12:07:26.370807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.085` n `13`; crypto_alt avg `0.0956` n `239`; crypto_major avg `0.14` n `8`; equity avg `0.1231` n `168`; fx avg `0.003` n `6`; index avg `0.0213` n `27`; metal avg `0.0758` n `20`; unknown avg `1.8343` n `1249`
- 1h: commodity avg `-0.0676` n `13`; crypto_alt avg `0.3636` n `239`; crypto_major avg `0.4743` n `8`; equity avg `0.4788` n `168`; fx avg `-0.0088` n `6`; index avg `0.0654` n `27`; metal avg `0.1318` n `20`; unknown avg `-0.2506` n `1253`
- 4h: commodity avg `0.0707` n `13`; crypto_alt avg `0.5384` n `239`; crypto_major avg `0.1246` n `8`; equity avg `0.2086` n `168`; fx avg `0.0036` n `6`; index avg `0.0366` n `27`; metal avg `0.0648` n `20`; unknown avg `130.8588` n `1157`
- 24h: commodity avg `0.4358` n `13`; crypto_alt avg `4.7419` n `239`; crypto_major avg `4.022` n `8`; equity avg `4.6745` n `168`; fx avg `0.084` n `6`; index avg `0.4691` n `27`; metal avg `0.9844` n `20`; unknown avg `191.0598` n `1053`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
