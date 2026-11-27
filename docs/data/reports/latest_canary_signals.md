# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T23:22:36.568910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `13`; crypto_alt avg `-0.1676` n `239`; crypto_major avg `-0.2481` n `8`; equity avg `-0.007` n `168`; fx avg `-0.0014` n `6`; index avg `-0.0052` n `27`; metal avg `-0.0057` n `20`; unknown avg `0.0174` n `1259`
- 1h: commodity avg `-0.0143` n `13`; crypto_alt avg `0.1643` n `239`; crypto_major avg `0.042` n `8`; equity avg `0.0846` n `168`; fx avg `-0.0056` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0029` n `20`; unknown avg `-0.0729` n `1247`
- 4h: commodity avg `0.0369` n `13`; crypto_alt avg `-0.0566` n `239`; crypto_major avg `-0.5941` n `8`; equity avg `-0.0799` n `168`; fx avg `-0.0126` n `6`; index avg `-0.01` n `27`; metal avg `0.17` n `20`; unknown avg `0.7538` n `1161`
- 24h: commodity avg `-0.5124` n `13`; crypto_alt avg `0.5386` n `239`; crypto_major avg `0.2186` n `8`; equity avg `3.4646` n `168`; fx avg `-0.166` n `6`; index avg `0.3235` n `27`; metal avg `1.0359` n `20`; unknown avg `211.9156` n `989`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
