# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T07:07:34.456941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `0.1812` n `239`; crypto_major avg `0.1888` n `8`; equity avg `0.1685` n `162`; fx avg `-0.0078` n `6`; index avg `0.0085` n `27`; metal avg `0.0333` n `20`; unknown avg `-0.0552` n `1240`
- 1h: commodity avg `0.0435` n `13`; crypto_alt avg `0.0004` n `239`; crypto_major avg `-0.061` n `8`; equity avg `0.0631` n `162`; fx avg `-0.0206` n `6`; index avg `0.0304` n `27`; metal avg `-0.0022` n `20`; unknown avg `-0.0173` n `1230`
- 4h: commodity avg `-0.0284` n `13`; crypto_alt avg `0.3376` n `239`; crypto_major avg `0.4179` n `8`; equity avg `-0.7598` n `162`; fx avg `-0.0287` n `6`; index avg `-0.0787` n `27`; metal avg `-0.0456` n `20`; unknown avg `-0.2727` n `1196`
- 24h: commodity avg `-1.1945` n `13`; crypto_alt avg `0.8982` n `239`; crypto_major avg `1.181` n `8`; equity avg `-2.5064` n `162`; fx avg `-0.0318` n `6`; index avg `-0.2409` n `27`; metal avg `-0.0181` n `20`; unknown avg `279.0595` n `1097`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
