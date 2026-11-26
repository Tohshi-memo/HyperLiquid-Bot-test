# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T11:07:28.361068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0884` n `13`; crypto_alt avg `0.1901` n `239`; crypto_major avg `0.0505` n `8`; equity avg `0.0855` n `168`; fx avg `-0.0041` n `6`; index avg `0.0136` n `27`; metal avg `-0.0133` n `20`; unknown avg `1.1789` n `1257`
- 1h: commodity avg `0.1656` n `13`; crypto_alt avg `-0.0641` n `239`; crypto_major avg `-0.5741` n `8`; equity avg `-0.2843` n `168`; fx avg `0.0056` n `6`; index avg `-0.0337` n `27`; metal avg `-0.1568` n `20`; unknown avg `0.0713` n `1261`
- 4h: commodity avg `0.1753` n `13`; crypto_alt avg `0.2607` n `239`; crypto_major avg `-0.2135` n `8`; equity avg `-0.1737` n `168`; fx avg `0.0494` n `6`; index avg `-0.0131` n `27`; metal avg `-0.0479` n `20`; unknown avg `305.8464` n `1151`
- 24h: commodity avg `0.5503` n `13`; crypto_alt avg `3.6676` n `239`; crypto_major avg `3.0472` n `8`; equity avg `3.321` n `168`; fx avg `0.097` n `6`; index avg `0.2989` n `27`; metal avg `0.6031` n `20`; unknown avg `441.3366` n `1019`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
