# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T18:52:49.466705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0898` n `13`; crypto_alt avg `-0.3027` n `239`; crypto_major avg `-0.2964` n `8`; equity avg `0.023` n `161`; fx avg `-0.0239` n `6`; index avg `0.0223` n `27`; metal avg `-0.0384` n `20`; unknown avg `1.8793` n `1260`
- 1h: commodity avg `0.1045` n `13`; crypto_alt avg `-0.6142` n `239`; crypto_major avg `-0.3897` n `8`; equity avg `-0.1523` n `161`; fx avg `0.0071` n `6`; index avg `0.0221` n `27`; metal avg `-0.0664` n `20`; unknown avg `1.7356` n `1256`
- 4h: commodity avg `-0.1435` n `13`; crypto_alt avg `-0.0519` n `239`; crypto_major avg `0.8359` n `8`; equity avg `2.1957` n `161`; fx avg `0.0205` n `6`; index avg `0.2446` n `27`; metal avg `-0.2632` n `20`; unknown avg `2.0737` n `1243`
- 24h: commodity avg `0.5277` n `13`; crypto_alt avg `0.5366` n `239`; crypto_major avg `1.3095` n `8`; equity avg `6.4453` n `161`; fx avg `-0.1629` n `6`; index avg `0.6312` n `27`; metal avg `0.061` n `20`; unknown avg `6.3183` n `1153`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
