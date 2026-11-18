# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T02:07:33.603419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0658` n `13`; crypto_alt avg `-0.191` n `239`; crypto_major avg `-0.2643` n `8`; equity avg `-0.209` n `163`; fx avg `0.0039` n `6`; index avg `-0.0221` n `27`; metal avg `-0.2072` n `20`; unknown avg `8.9822` n `1260`
- 1h: commodity avg `-0.1355` n `13`; crypto_alt avg `-0.5284` n `239`; crypto_major avg `-0.685` n `8`; equity avg `-1.2483` n `163`; fx avg `0.0132` n `6`; index avg `-0.1588` n `27`; metal avg `-0.2949` n `20`; unknown avg `8.3927` n `1262`
- 4h: commodity avg `-0.1868` n `13`; crypto_alt avg `-0.0899` n `239`; crypto_major avg `-0.0034` n `8`; equity avg `-0.1249` n `163`; fx avg `-0.0613` n `6`; index avg `-0.0819` n `27`; metal avg `-0.4847` n `20`; unknown avg `5.6045` n `1215`
- 24h: commodity avg `0.1775` n `13`; crypto_alt avg `0.2341` n `239`; crypto_major avg `0.165` n `8`; equity avg `-0.3309` n `163`; fx avg `-0.088` n `6`; index avg `-0.1339` n `27`; metal avg `-0.6704` n `20`; unknown avg `7.086` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
