# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T02:37:35.114303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.035` n `13`; crypto_alt avg `-0.0812` n `239`; crypto_major avg `0.1217` n `8`; equity avg `0.337` n `163`; fx avg `-0.0121` n `6`; index avg `0.0592` n `27`; metal avg `0.0124` n `20`; unknown avg `2.2837` n `1266`
- 1h: commodity avg `-0.0355` n `13`; crypto_alt avg `-0.1538` n `239`; crypto_major avg `-0.003` n `8`; equity avg `-0.4564` n `163`; fx avg `-0.017` n `6`; index avg `-0.0314` n `27`; metal avg `-0.2864` n `20`; unknown avg `4.0957` n `1264`
- 4h: commodity avg `-0.1445` n `13`; crypto_alt avg `-0.4238` n `239`; crypto_major avg `-0.0963` n `8`; equity avg `-0.8374` n `163`; fx avg `-0.1001` n `6`; index avg `-0.1449` n `27`; metal avg `-0.4682` n `20`; unknown avg `2.4367` n `1217`
- 24h: commodity avg `0.2534` n `13`; crypto_alt avg `0.4438` n `239`; crypto_major avg `0.8483` n `8`; equity avg `-0.2864` n `163`; fx avg `-0.1109` n `6`; index avg `-0.1069` n `27`; metal avg `-0.6591` n `20`; unknown avg `6.9978` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
