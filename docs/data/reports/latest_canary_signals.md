# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T17:07:24.136044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.045` n `13`; crypto_alt avg `0.2071` n `239`; crypto_major avg `0.1211` n `8`; equity avg `-0.1287` n `161`; fx avg `-0.0087` n `6`; index avg `-0.002` n `27`; metal avg `0.0109` n `20`; unknown avg `0.6802` n `1258`
- 1h: commodity avg `-0.1047` n `13`; crypto_alt avg `0.1938` n `239`; crypto_major avg `0.2596` n `8`; equity avg `0.266` n `161`; fx avg `-0.0188` n `6`; index avg `0.0429` n `27`; metal avg `-0.1017` n `20`; unknown avg `0.0584` n `1255`
- 4h: commodity avg `0.1131` n `13`; crypto_alt avg `0.8705` n `239`; crypto_major avg `1.0624` n `8`; equity avg `1.634` n `161`; fx avg `0.0012` n `6`; index avg `0.1496` n `27`; metal avg `-0.3407` n `20`; unknown avg `-0.1042` n `1225`
- 24h: commodity avg `0.5502` n `13`; crypto_alt avg `2.5172` n `239`; crypto_major avg `2.6198` n `8`; equity avg `6.606` n `161`; fx avg `-0.1265` n `6`; index avg `0.6199` n `27`; metal avg `0.2292` n `20`; unknown avg `4.2422` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
