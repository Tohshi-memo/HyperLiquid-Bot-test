# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T14:52:38.973876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.4` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.0096` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0635` n `12`; crypto_alt avg `0.1518` n `234`; crypto_major avg `0.0824` n `8`; equity avg `0.1831` n `142`; fx avg `-0.0276` n `6`; index avg `0.0495` n `26`; metal avg `0.053` n `20`; unknown avg `1.8115` n `963`
- 1h: commodity avg `0.1518` n `12`; crypto_alt avg `-0.7847` n `234`; crypto_major avg `-0.9352` n `8`; equity avg `0.0854` n `142`; fx avg `-0.0056` n `6`; index avg `0.0744` n `26`; metal avg `-0.0367` n `20`; unknown avg `3.6122` n `907`
- 4h: commodity avg `0.1004` n `12`; crypto_alt avg `-0.3355` n `234`; crypto_major avg `-0.5546` n `8`; equity avg `0.1217` n `142`; fx avg `-0.0417` n `6`; index avg `0.1405` n `26`; metal avg `-0.1345` n `20`; unknown avg `5.6649` n `901`
- 24h: commodity avg `0.0729` n `12`; crypto_alt avg `-1.0672` n `234`; crypto_major avg `-1.1091` n `8`; equity avg `-0.5293` n `142`; fx avg `0.0037` n `6`; index avg `0.0936` n `26`; metal avg `-0.0348` n `20`; unknown avg `9159.0244` n `840`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
