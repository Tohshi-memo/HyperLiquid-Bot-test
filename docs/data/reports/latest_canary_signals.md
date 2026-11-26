# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T13:07:28.571325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `13`; crypto_alt avg `-0.0293` n `239`; crypto_major avg `-0.0132` n `8`; equity avg `-0.0613` n `168`; fx avg `-0.0004` n `6`; index avg `-0.0153` n `27`; metal avg `-0.063` n `20`; unknown avg `0.0268` n `1257`
- 1h: commodity avg `0.108` n `13`; crypto_alt avg `-0.1597` n `239`; crypto_major avg `0.0197` n `8`; equity avg `0.0234` n `168`; fx avg `0.0081` n `6`; index avg `-0.0152` n `27`; metal avg `-0.0909` n `20`; unknown avg `8.4062` n `1257`
- 4h: commodity avg `0.2513` n `13`; crypto_alt avg `0.1325` n `239`; crypto_major avg `-0.1763` n `8`; equity avg `0.0855` n `168`; fx avg `0.0253` n `6`; index avg `0.0015` n `27`; metal avg `-0.1479` n `20`; unknown avg `1.7115` n `1247`
- 24h: commodity avg `0.3752` n `13`; crypto_alt avg `4.7398` n `239`; crypto_major avg `3.8723` n `8`; equity avg `4.4891` n `168`; fx avg `0.0938` n `6`; index avg `0.4138` n `27`; metal avg `0.6833` n `20`; unknown avg `238.9056` n `1053`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
