# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T14:07:35.152094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0325` n `13`; crypto_alt avg `0.0375` n `237`; crypto_major avg `0.0275` n `8`; equity avg `0.1339` n `152`; fx avg `0.0192` n `6`; index avg `0.0245` n `26`; metal avg `-0.0502` n `20`; unknown avg `0.1646` n `1175`
- 1h: commodity avg `0.1931` n `13`; crypto_alt avg `0.1729` n `237`; crypto_major avg `0.3952` n `8`; equity avg `0.273` n `152`; fx avg `0.0338` n `6`; index avg `0.0516` n `26`; metal avg `-0.0502` n `20`; unknown avg `0.0164` n `1167`
- 4h: commodity avg `-0.014` n `13`; crypto_alt avg `0.1488` n `237`; crypto_major avg `0.2558` n `8`; equity avg `-0.274` n `152`; fx avg `0.0211` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0087` n `20`; unknown avg `-0.2685` n `1161`
- 24h: commodity avg `0.3613` n `13`; crypto_alt avg `0.1656` n `237`; crypto_major avg `0.4017` n `8`; equity avg `-1.4338` n `152`; fx avg `-0.053` n `6`; index avg `-0.2296` n `26`; metal avg `-0.3392` n `20`; unknown avg `-0.6924` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2122`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1705`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
