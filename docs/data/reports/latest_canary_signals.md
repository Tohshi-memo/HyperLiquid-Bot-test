# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T06:52:28.970845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `13`; crypto_alt avg `0.0135` n `239`; crypto_major avg `0.0978` n `8`; equity avg `0.1087` n `166`; fx avg `-0.0203` n `6`; index avg `0.0117` n `27`; metal avg `0.0421` n `20`; unknown avg `0.0701` n `1266`
- 1h: commodity avg `-0.2157` n `13`; crypto_alt avg `-0.0026` n `239`; crypto_major avg `-0.264` n `8`; equity avg `-0.1894` n `166`; fx avg `-0.0091` n `6`; index avg `-0.0519` n `27`; metal avg `-0.0271` n `20`; unknown avg `161.5057` n `1242`
- 4h: commodity avg `-0.0884` n `13`; crypto_alt avg `1.8635` n `239`; crypto_major avg `1.5559` n `8`; equity avg `1.6417` n `166`; fx avg `0.0089` n `6`; index avg `0.0938` n `27`; metal avg `0.4075` n `20`; unknown avg `-0.0285` n `1229`
- 24h: commodity avg `-0.4966` n `13`; crypto_alt avg `2.4583` n `239`; crypto_major avg `3.2037` n `8`; equity avg `2.4808` n `166`; fx avg `0.2057` n `6`; index avg `0.1652` n `27`; metal avg `0.5728` n `20`; unknown avg `339.8888` n `1019`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
