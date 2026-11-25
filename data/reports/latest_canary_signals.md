# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T22:22:27.739176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `0.0407` n `239`; crypto_major avg `-0.1053` n `8`; equity avg `0.04` n `168`; fx avg `-0.0003` n `6`; index avg `-0.0143` n `27`; metal avg `0.006` n `20`; unknown avg `19.961` n `1255`
- 1h: commodity avg `0.0153` n `13`; crypto_alt avg `-0.0038` n `239`; crypto_major avg `-0.2813` n `8`; equity avg `-0.2455` n `168`; fx avg `-0.0045` n `6`; index avg `-0.0288` n `27`; metal avg `0.16` n `20`; unknown avg `43.0864` n `1241`
- 4h: commodity avg `-0.0132` n `13`; crypto_alt avg `0.9836` n `239`; crypto_major avg `0.9471` n `8`; equity avg `1.4521` n `168`; fx avg `-0.0102` n `6`; index avg `0.1029` n `27`; metal avg `0.5715` n `20`; unknown avg `195.7931` n `1199`
- 24h: commodity avg `0.4394` n `13`; crypto_alt avg `2.3612` n `239`; crypto_major avg `0.931` n `8`; equity avg `-0.8421` n `168`; fx avg `0.0442` n `6`; index avg `-0.092` n `27`; metal avg `0.2477` n `20`; unknown avg `1.3121` n `1059`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
