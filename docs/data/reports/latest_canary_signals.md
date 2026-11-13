# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T00:07:30.161636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `13`; crypto_alt avg `0.159` n `239`; crypto_major avg `0.0919` n `8`; equity avg `0.2978` n `162`; fx avg `0.0225` n `6`; index avg `0.0422` n `27`; metal avg `0.0426` n `20`; unknown avg `0.4004` n `1249`
- 1h: commodity avg `-0.0376` n `13`; crypto_alt avg `0.1017` n `239`; crypto_major avg `0.1676` n `8`; equity avg `0.6105` n `162`; fx avg `0.0074` n `6`; index avg `0.0585` n `27`; metal avg `0.0823` n `20`; unknown avg `1.3252` n `1251`
- 4h: commodity avg `-0.0539` n `13`; crypto_alt avg `0.7263` n `239`; crypto_major avg `0.5293` n `8`; equity avg `1.274` n `162`; fx avg `0.0035` n `6`; index avg `0.1357` n `27`; metal avg `0.0828` n `20`; unknown avg `43.6412` n `1195`
- 24h: commodity avg `0.859` n `13`; crypto_alt avg `-0.7662` n `239`; crypto_major avg `-1.528` n `8`; equity avg `0.1546` n `162`; fx avg `-0.054` n `6`; index avg `0.1048` n `27`; metal avg `-0.46` n `20`; unknown avg `51.045` n `1119`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
