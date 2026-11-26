# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T07:37:23.301402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0384` n `13`; crypto_alt avg `0.0117` n `239`; crypto_major avg `0.0452` n `8`; equity avg `0.0561` n `168`; fx avg `0.0153` n `6`; index avg `0.0074` n `27`; metal avg `0.0071` n `20`; unknown avg `157.9466` n `1267`
- 1h: commodity avg `0.0309` n `13`; crypto_alt avg `-0.1108` n `239`; crypto_major avg `-0.0312` n `8`; equity avg `0.166` n `168`; fx avg `0.0413` n `6`; index avg `0.0322` n `27`; metal avg `0.0827` n `20`; unknown avg `18.7917` n `1261`
- 4h: commodity avg `-0.2787` n `13`; crypto_alt avg `-0.3124` n `239`; crypto_major avg `-0.2771` n `8`; equity avg `-0.3942` n `168`; fx avg `0.0183` n `6`; index avg `-0.034` n `27`; metal avg `-0.082` n `20`; unknown avg `0.5373` n `1221`
- 24h: commodity avg `0.6849` n `13`; crypto_alt avg `3.6426` n `239`; crypto_major avg `3.7273` n `8`; equity avg `3.6858` n `168`; fx avg `0.1204` n `6`; index avg `0.301` n `27`; metal avg `0.7418` n `20`; unknown avg `760.4245` n `1031`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
