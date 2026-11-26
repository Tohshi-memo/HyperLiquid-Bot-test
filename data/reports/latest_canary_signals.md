# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T14:07:27.668284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0352` n `13`; crypto_alt avg `0.0255` n `239`; crypto_major avg `-0.0081` n `8`; equity avg `-0.1019` n `168`; fx avg `0.0135` n `6`; index avg `-0.0156` n `27`; metal avg `-0.0398` n `20`; unknown avg `144.5216` n `1257`
- 1h: commodity avg `-0.0109` n `13`; crypto_alt avg `0.063` n `239`; crypto_major avg `0.0987` n `8`; equity avg `-0.0677` n `168`; fx avg `0.0183` n `6`; index avg `-0.0078` n `27`; metal avg `0.0128` n `20`; unknown avg `142.711` n `1263`
- 4h: commodity avg `0.1951` n `13`; crypto_alt avg `0.2076` n `239`; crypto_major avg `0.0143` n `8`; equity avg `0.1474` n `168`; fx avg `0.0231` n `6`; index avg `0.0085` n `27`; metal avg `-0.1037` n `20`; unknown avg `29.1085` n `1251`
- 24h: commodity avg `0.4152` n `13`; crypto_alt avg `5.5555` n `239`; crypto_major avg `5.1014` n `8`; equity avg `5.1792` n `168`; fx avg `0.0791` n `6`; index avg `0.4689` n `27`; metal avg `0.9764` n `20`; unknown avg `1.6476` n `1055`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
