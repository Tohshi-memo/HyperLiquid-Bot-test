# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T06:37:26.895667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2137` n `13`; crypto_alt avg `0.1108` n `239`; crypto_major avg `0.1318` n `8`; equity avg `0.0941` n `168`; fx avg `-0.0094` n `6`; index avg `0.0045` n `27`; metal avg `-0.0315` n `20`; unknown avg `1.7881` n `1263`
- 1h: commodity avg `-0.3363` n `13`; crypto_alt avg `-0.1422` n `239`; crypto_major avg `-0.6499` n `8`; equity avg `-0.769` n `168`; fx avg `-0.004` n `6`; index avg `-0.1062` n `27`; metal avg `-0.3927` n `20`; unknown avg `0.562` n `1239`
- 4h: commodity avg `-0.2426` n `13`; crypto_alt avg `-0.3872` n `239`; crypto_major avg `-0.3551` n `8`; equity avg `-0.7667` n `168`; fx avg `-0.0004` n `6`; index avg `-0.0882` n `27`; metal avg `-0.3715` n `20`; unknown avg `2.5877` n `1221`
- 24h: commodity avg `0.5037` n `13`; crypto_alt avg `2.3514` n `239`; crypto_major avg `2.5367` n `8`; equity avg `2.1274` n `168`; fx avg `0.0328` n `6`; index avg `0.1299` n `27`; metal avg `0.6265` n `20`; unknown avg `761.75` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
