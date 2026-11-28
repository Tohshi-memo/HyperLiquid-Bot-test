# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T01:52:32.781455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `13`; crypto_alt avg `0.039` n `239`; crypto_major avg `0.1406` n `8`; equity avg `0.0001` n `168`; fx avg `-0.0021` n `6`; index avg `0.0014` n `27`; metal avg `0.0029` n `20`; unknown avg `4.3964` n `1265`
- 1h: commodity avg `0.0419` n `13`; crypto_alt avg `0.2498` n `239`; crypto_major avg `0.5557` n `8`; equity avg `0.0955` n `168`; fx avg `0.002` n `6`; index avg `0.0147` n `27`; metal avg `0.0002` n `20`; unknown avg `1.5697` n `1257`
- 4h: commodity avg `-0.09` n `13`; crypto_alt avg `0.2698` n `239`; crypto_major avg `0.5888` n `8`; equity avg `0.0914` n `168`; fx avg `-0.0097` n `6`; index avg `0.0079` n `27`; metal avg `0.017` n `20`; unknown avg `2.1818` n `1233`
- 24h: commodity avg `-0.7058` n `13`; crypto_alt avg `0.4119` n `239`; crypto_major avg `0.6521` n `8`; equity avg `2.5788` n `168`; fx avg `-0.15` n `6`; index avg `0.2408` n `27`; metal avg `0.6788` n `20`; unknown avg `291.3736` n `989`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
