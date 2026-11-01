# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T07:07:27.607521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `-0.0078` n `238`; crypto_major avg `-0.0206` n `8`; equity avg `0.0251` n `156`; fx avg `-0.0025` n `6`; index avg `0.0099` n `27`; metal avg `0.0006` n `20`; unknown avg `0.2935` n `1257`
- 1h: commodity avg `-0.008` n `13`; crypto_alt avg `-0.2` n `238`; crypto_major avg `-0.0685` n `8`; equity avg `0.0261` n `156`; fx avg `-0.0056` n `6`; index avg `0.0194` n `27`; metal avg `0.0279` n `20`; unknown avg `0.4164` n `1254`
- 4h: commodity avg `0.0222` n `13`; crypto_alt avg `0.4742` n `238`; crypto_major avg `0.2155` n `8`; equity avg `0.2658` n `156`; fx avg `-0.018` n `6`; index avg `0.0357` n `27`; metal avg `0.0306` n `20`; unknown avg `0.5707` n `1226`
- 24h: commodity avg `-0.0351` n `13`; crypto_alt avg `0.5497` n `238`; crypto_major avg `0.4125` n `8`; equity avg `0.3186` n `156`; fx avg `-0.0141` n `6`; index avg `0.0244` n `27`; metal avg `0.0669` n `20`; unknown avg `2.5608` n `996`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
