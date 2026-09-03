# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T04:22:25.065792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.039` n `12`; crypto_alt avg `-0.0503` n `232`; crypto_major avg `-0.2248` n `8`; equity avg `-0.0079` n `133`; fx avg `-0.0101` n `6`; index avg `0.0048` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.0296` n `792`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `-0.0073` n `232`; crypto_major avg `-0.2147` n `8`; equity avg `0.0972` n `133`; fx avg `-0.0094` n `6`; index avg `0.0108` n `26`; metal avg `0.0385` n `20`; unknown avg `-0.0758` n `790`
- 4h: commodity avg `0.0074` n `12`; crypto_alt avg `0.8767` n `232`; crypto_major avg `0.7384` n `8`; equity avg `0.4841` n `133`; fx avg `-0.1254` n `6`; index avg `0.0988` n `26`; metal avg `0.2469` n `20`; unknown avg `15.8953` n `790`
- 24h: commodity avg `0.19` n `12`; crypto_alt avg `0.5323` n `232`; crypto_major avg `0.4096` n `8`; equity avg `1.7602` n `133`; fx avg `-0.3978` n `6`; index avg `0.2286` n `26`; metal avg `0.9317` n `20`; unknown avg `-0.4592` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
