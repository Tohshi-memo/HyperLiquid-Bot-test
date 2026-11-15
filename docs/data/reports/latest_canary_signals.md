# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T13:07:24.015436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `-0.0789` n `239`; crypto_major avg `0.0918` n `8`; equity avg `0.0188` n `162`; fx avg `-0.0024` n `6`; index avg `0.0025` n `27`; metal avg `-0.0099` n `20`; unknown avg `159.1383` n `1257`
- 1h: commodity avg `0.0205` n `13`; crypto_alt avg `0.3723` n `239`; crypto_major avg `0.4672` n `8`; equity avg `0.0598` n `162`; fx avg `-0.0023` n `6`; index avg `0.0007` n `27`; metal avg `0.0089` n `20`; unknown avg `317.7003` n `1259`
- 4h: commodity avg `-0.0126` n `13`; crypto_alt avg `0.5335` n `239`; crypto_major avg `0.5011` n `8`; equity avg `0.0026` n `162`; fx avg `-0.0248` n `6`; index avg `-0.0094` n `27`; metal avg `0.014` n `20`; unknown avg `0.2653` n `1251`
- 24h: commodity avg `0.0532` n `13`; crypto_alt avg `-3.0254` n `239`; crypto_major avg `-2.1992` n `8`; equity avg `-0.5281` n `162`; fx avg `-0.0001` n `6`; index avg `-0.0523` n `27`; metal avg `-0.3139` n `20`; unknown avg `260.7786` n `1134`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
