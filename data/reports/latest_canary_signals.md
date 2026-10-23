# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T23:52:26.862711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `13`; crypto_alt avg `0.4066` n `237`; crypto_major avg `0.2681` n `8`; equity avg `0.0966` n `152`; fx avg `-0.0068` n `6`; index avg `0.008` n `26`; metal avg `0.0217` n `20`; unknown avg `0.7468` n `1228`
- 1h: commodity avg `-0.0291` n `13`; crypto_alt avg `1.0032` n `237`; crypto_major avg `0.5532` n `8`; equity avg `0.1658` n `152`; fx avg `-0.0279` n `6`; index avg `0.0129` n `26`; metal avg `0.0784` n `20`; unknown avg `4.1152` n `1224`
- 4h: commodity avg `0.0933` n `13`; crypto_alt avg `-0.9676` n `237`; crypto_major avg `-0.3791` n `8`; equity avg `0.0126` n `152`; fx avg `-0.0067` n `6`; index avg `-0.0023` n `26`; metal avg `-0.054` n `20`; unknown avg `109.0478` n `1128`
- 24h: commodity avg `0.4615` n `13`; crypto_alt avg `-0.55` n `237`; crypto_major avg `-0.1863` n `8`; equity avg `1.5432` n `152`; fx avg `-0.071` n `6`; index avg `0.0905` n `26`; metal avg `-0.1475` n `20`; unknown avg `200.5682` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2023`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
