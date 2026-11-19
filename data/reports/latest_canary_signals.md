# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T14:37:33.985166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `13`; crypto_alt avg `0.0206` n `239`; crypto_major avg `0.1614` n `8`; equity avg `0.7012` n `165`; fx avg `-0.0156` n `6`; index avg `0.0294` n `27`; metal avg `0.0114` n `20`; unknown avg `0.4306` n `1265`
- 1h: commodity avg `0.0563` n `13`; crypto_alt avg `-0.057` n `239`; crypto_major avg `0.2234` n `8`; equity avg `0.8895` n `165`; fx avg `-0.0013` n `6`; index avg `0.0438` n `27`; metal avg `-0.0559` n `20`; unknown avg `0.212` n `1263`
- 4h: commodity avg `0.1543` n `13`; crypto_alt avg `0.1911` n `239`; crypto_major avg `0.5493` n `8`; equity avg `0.5517` n `165`; fx avg `-0.0394` n `6`; index avg `-0.0072` n `27`; metal avg `-0.189` n `20`; unknown avg `0.2293` n `1257`
- 24h: commodity avg `0.3617` n `13`; crypto_alt avg `0.8697` n `239`; crypto_major avg `1.3888` n `8`; equity avg `3.5906` n `165`; fx avg `0.0364` n `6`; index avg `0.4348` n `27`; metal avg `-0.255` n `20`; unknown avg `2.8159` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
