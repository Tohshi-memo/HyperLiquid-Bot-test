# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T01:22:28.469370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `13`; crypto_alt avg `0.2105` n `239`; crypto_major avg `0.3101` n `8`; equity avg `0.1869` n `168`; fx avg `-0.0102` n `6`; index avg `0.0178` n `27`; metal avg `0.0126` n `20`; unknown avg `0.004` n `1263`
- 1h: commodity avg `-0.1014` n `13`; crypto_alt avg `0.1703` n `239`; crypto_major avg `0.4692` n `8`; equity avg `0.0431` n `168`; fx avg `0.0096` n `6`; index avg `0.0002` n `27`; metal avg `0.003` n `20`; unknown avg `0.535` n `1257`
- 4h: commodity avg `-0.0864` n `13`; crypto_alt avg `0.248` n `239`; crypto_major avg `0.3494` n `8`; equity avg `0.0332` n `168`; fx avg `-0.0022` n `6`; index avg `0.0177` n `27`; metal avg `0.0091` n `20`; unknown avg `0.6294` n `1213`
- 24h: commodity avg `-0.6759` n `13`; crypto_alt avg `0.302` n `239`; crypto_major avg `0.3964` n `8`; equity avg `2.7457` n `168`; fx avg `-0.1238` n `6`; index avg `0.254` n `27`; metal avg `0.8888` n `20`; unknown avg `290.5395` n `989`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
