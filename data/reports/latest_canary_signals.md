# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T09:52:28.623012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `13`; crypto_alt avg `-0.0712` n `239`; crypto_major avg `-0.0196` n `8`; equity avg `0.0032` n `168`; fx avg `0.0058` n `6`; index avg `0.0012` n `27`; metal avg `-0.0123` n `20`; unknown avg `0.8379` n `1265`
- 1h: commodity avg `0.0034` n `13`; crypto_alt avg `0.0333` n `239`; crypto_major avg `-0.0913` n `8`; equity avg `-0.2445` n `168`; fx avg `0.0196` n `6`; index avg `-0.0408` n `27`; metal avg `-0.0376` n `20`; unknown avg `79.6013` n `1255`
- 4h: commodity avg `-0.2648` n `13`; crypto_alt avg `-0.0979` n `239`; crypto_major avg `-0.1957` n `8`; equity avg `-0.3668` n `168`; fx avg `0.0574` n `6`; index avg `-0.0614` n `27`; metal avg `-0.0264` n `20`; unknown avg `177.8932` n `1131`
- 24h: commodity avg `0.2599` n `13`; crypto_alt avg `3.8317` n `239`; crypto_major avg `4.0649` n `8`; equity avg `4.0389` n `168`; fx avg `0.1097` n `6`; index avg `0.3257` n `27`; metal avg `0.8001` n `20`; unknown avg `646.1248` n `999`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
