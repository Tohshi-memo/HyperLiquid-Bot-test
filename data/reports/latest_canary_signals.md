# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T20:07:25.689314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `13`; crypto_alt avg `-0.032` n `239`; crypto_major avg `-0.0358` n `8`; equity avg `0.0077` n `168`; fx avg `-0.0076` n `6`; index avg `-0.0057` n `27`; metal avg `0.0263` n `20`; unknown avg `-0.1345` n `1243`
- 1h: commodity avg `0.1245` n `13`; crypto_alt avg `-0.0332` n `239`; crypto_major avg `-0.0326` n `8`; equity avg `0.0222` n `168`; fx avg `-0.0149` n `6`; index avg `-0.0141` n `27`; metal avg `0.1507` n `20`; unknown avg `64.7946` n `1251`
- 4h: commodity avg `-0.0376` n `13`; crypto_alt avg `0.1446` n `239`; crypto_major avg `-0.1715` n `8`; equity avg `0.6049` n `168`; fx avg `-0.0436` n `6`; index avg `0.0423` n `27`; metal avg `0.2699` n `20`; unknown avg `163.0934` n `1222`
- 24h: commodity avg `-0.4854` n `13`; crypto_alt avg `-0.1593` n `239`; crypto_major avg `-0.031` n `8`; equity avg `3.1799` n `168`; fx avg `-0.1585` n `6`; index avg `0.2987` n `27`; metal avg `0.9444` n `20`; unknown avg `268.1208` n `1039`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
