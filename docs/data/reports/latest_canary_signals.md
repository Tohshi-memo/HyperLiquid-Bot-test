# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T10:52:34.511828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0969` n `13`; crypto_alt avg `-0.0472` n `234`; crypto_major avg `-0.1241` n `8`; equity avg `-0.0413` n `142`; fx avg `0.0158` n `6`; index avg `-0.0015` n `26`; metal avg `0.0658` n `20`; unknown avg `1.0919` n `985`
- 1h: commodity avg `0.1289` n `13`; crypto_alt avg `-0.112` n `234`; crypto_major avg `0.0055` n `8`; equity avg `-0.1707` n `142`; fx avg `0.0092` n `6`; index avg `-0.0156` n `26`; metal avg `0.0062` n `20`; unknown avg `0.6962` n `981`
- 4h: commodity avg `-0.4171` n `13`; crypto_alt avg `0.4337` n `234`; crypto_major avg `0.4348` n `8`; equity avg `0.4462` n `142`; fx avg `-0.0761` n `6`; index avg `0.1155` n `26`; metal avg `0.0402` n `20`; unknown avg `-0.5936` n `907`
- 24h: commodity avg `-0.2905` n `13`; crypto_alt avg `1.8102` n `234`; crypto_major avg `1.9165` n `8`; equity avg `0.7907` n `142`; fx avg `-0.3119` n `6`; index avg `0.1414` n `26`; metal avg `0.0691` n `20`; unknown avg `-0.1936` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
