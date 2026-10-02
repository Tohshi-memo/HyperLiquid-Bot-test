# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T02:22:47.598968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `13`; crypto_alt avg `-0.0528` n `234`; crypto_major avg `-0.1636` n `8`; equity avg `0.0464` n `142`; fx avg `-0.0204` n `6`; index avg `0.0052` n `26`; metal avg `0.0374` n `20`; unknown avg `0.1283` n `985`
- 1h: commodity avg `-0.007` n `13`; crypto_alt avg `0.7455` n `234`; crypto_major avg `0.5364` n `8`; equity avg `0.1045` n `142`; fx avg `-0.0644` n `6`; index avg `0.0411` n `26`; metal avg `0.0853` n `20`; unknown avg `0.9614` n `983`
- 4h: commodity avg `-0.1768` n `13`; crypto_alt avg `0.6867` n `234`; crypto_major avg `0.3518` n `8`; equity avg `0.1555` n `142`; fx avg `-0.0384` n `6`; index avg `0.0543` n `26`; metal avg `-0.106` n `20`; unknown avg `0.1877` n `977`
- 24h: commodity avg `-0.0218` n `13`; crypto_alt avg `0.2918` n `234`; crypto_major avg `0.4068` n `8`; equity avg `0.8205` n `142`; fx avg `-0.2354` n `6`; index avg `0.1177` n `26`; metal avg `-0.138` n `20`; unknown avg `0.1529` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
