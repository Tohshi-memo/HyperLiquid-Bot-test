# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T09:37:29.051168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0471` n `13`; crypto_alt avg `0.0387` n `239`; crypto_major avg `0.1441` n `8`; equity avg `0.0887` n `168`; fx avg `0.0012` n `6`; index avg `0.0195` n `27`; metal avg `0.0428` n `20`; unknown avg `0.1063` n `1267`
- 1h: commodity avg `-0.11` n `13`; crypto_alt avg `0.1971` n `239`; crypto_major avg `0.1687` n `8`; equity avg `0.0948` n `168`; fx avg `0.0219` n `6`; index avg `-0.0119` n `27`; metal avg `0.0963` n `20`; unknown avg `121.3818` n `1261`
- 4h: commodity avg `-0.3292` n `13`; crypto_alt avg `0.0819` n `239`; crypto_major avg `-0.4496` n `8`; equity avg `-0.687` n `168`; fx avg `0.0481` n `6`; index avg `-0.0975` n `27`; metal avg `-0.2257` n `20`; unknown avg `133.5524` n `1135`
- 24h: commodity avg `0.277` n `13`; crypto_alt avg `3.5496` n `239`; crypto_major avg `3.7487` n `8`; equity avg `3.6211` n `168`; fx avg `0.0825` n `6`; index avg `0.2695` n `27`; metal avg `0.7648` n `20`; unknown avg `450.0589` n `999`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
