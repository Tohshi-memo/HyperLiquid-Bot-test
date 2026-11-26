# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T12:22:35.828229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `13`; crypto_alt avg `-0.1776` n `239`; crypto_major avg `-0.2989` n `8`; equity avg `-0.0344` n `168`; fx avg `-0.0006` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0767` n `20`; unknown avg `8.6504` n `1265`
- 1h: commodity avg `-0.0723` n `13`; crypto_alt avg `-0.0406` n `239`; crypto_major avg `-0.1415` n `8`; equity avg `0.1951` n `168`; fx avg `0.0078` n `6`; index avg `0.025` n `27`; metal avg `-0.0366` n `20`; unknown avg `160.4882` n `1255`
- 4h: commodity avg `0.0039` n `13`; crypto_alt avg `0.29` n `239`; crypto_major avg `-0.1705` n `8`; equity avg `0.3962` n `168`; fx avg `0.0169` n `6`; index avg `0.0448` n `27`; metal avg `0.021` n `20`; unknown avg `172.9895` n `1183`
- 24h: commodity avg `0.2631` n `13`; crypto_alt avg `4.2201` n `239`; crypto_major avg `3.4506` n `8`; equity avg `4.4468` n `168`; fx avg `0.0534` n `6`; index avg `0.4423` n `27`; metal avg `0.7354` n `20`; unknown avg `191.0368` n `1057`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
