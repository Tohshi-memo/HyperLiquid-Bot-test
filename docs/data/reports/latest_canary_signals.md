# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T18:22:27.962919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.2759` n `235`; crypto_major avg `-0.2223` n `8`; equity avg `0.0089` n `151`; fx avg `0.0147` n `6`; index avg `0.0029` n `26`; metal avg `0.0138` n `20`; unknown avg `0.1108` n `1135`
- 1h: commodity avg `0.0345` n `13`; crypto_alt avg `-0.1198` n `235`; crypto_major avg `-0.1587` n `8`; equity avg `0.2185` n `151`; fx avg `0.0251` n `6`; index avg `0.0298` n `26`; metal avg `0.0296` n `20`; unknown avg `-0.5018` n `1133`
- 4h: commodity avg `0.3627` n `13`; crypto_alt avg `-0.4897` n `235`; crypto_major avg `-0.5303` n `8`; equity avg `0.1445` n `151`; fx avg `0.0165` n `6`; index avg `0.0436` n `26`; metal avg `-0.0703` n `20`; unknown avg `0.2078` n `1109`
- 24h: commodity avg `0.456` n `13`; crypto_alt avg `-1.6393` n `235`; crypto_major avg `-0.4434` n `8`; equity avg `-0.8533` n `151`; fx avg `0.168` n `6`; index avg `-0.1597` n `26`; metal avg `-0.2321` n `20`; unknown avg `0.1651` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1637`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1478`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0922`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0903`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
