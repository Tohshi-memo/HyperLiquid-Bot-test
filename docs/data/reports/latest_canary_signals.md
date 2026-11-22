# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T18:37:39.189764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `13`; crypto_alt avg `-0.0894` n `239`; crypto_major avg `0.0968` n `8`; equity avg `0.022` n `166`; fx avg `-0.0021` n `6`; index avg `0.0044` n `27`; metal avg `-0.0181` n `20`; unknown avg `158.1602` n `1264`
- 1h: commodity avg `-0.0233` n `13`; crypto_alt avg `-0.5629` n `239`; crypto_major avg `-0.1825` n `8`; equity avg `0.042` n `166`; fx avg `0.0037` n `6`; index avg `0.0079` n `27`; metal avg `-0.026` n `20`; unknown avg `39.6814` n `1253`
- 4h: commodity avg `-0.0341` n `13`; crypto_alt avg `-0.3243` n `239`; crypto_major avg `0.388` n `8`; equity avg `0.2118` n `166`; fx avg `0.0285` n `6`; index avg `0.0198` n `27`; metal avg `0.0469` n `20`; unknown avg `253.7268` n `1229`
- 24h: commodity avg `-0.0853` n `13`; crypto_alt avg `0.1789` n `239`; crypto_major avg `0.7437` n `8`; equity avg `1.0468` n `166`; fx avg `-0.0104` n `6`; index avg `0.1858` n `27`; metal avg `0.0268` n `20`; unknown avg `235.4533` n `1060`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
