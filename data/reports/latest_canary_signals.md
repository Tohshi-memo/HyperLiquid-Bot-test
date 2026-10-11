# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T15:37:27.788337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.3553` n `235`; crypto_major avg `0.2161` n `8`; equity avg `0.0343` n `150`; fx avg `-0.0036` n `6`; index avg `0.0007` n `26`; metal avg `0.0035` n `20`; unknown avg `1.4037` n `1134`
- 1h: commodity avg `0.1227` n `13`; crypto_alt avg `0.4774` n `235`; crypto_major avg `0.2705` n `8`; equity avg `0.036` n `150`; fx avg `0.0053` n `6`; index avg `0.0012` n `26`; metal avg `-0.0056` n `20`; unknown avg `3.224` n `1132`
- 4h: commodity avg `-0.108` n `13`; crypto_alt avg `1.5389` n `235`; crypto_major avg `0.5892` n `8`; equity avg `0.1378` n `150`; fx avg `-0.0168` n `6`; index avg `0.0139` n `26`; metal avg `0.0115` n `20`; unknown avg `4.7366` n `1053`
- 24h: commodity avg `0.2284` n `13`; crypto_alt avg `1.6282` n `235`; crypto_major avg `-0.0385` n `8`; equity avg `0.089` n `150`; fx avg `0.0125` n `6`; index avg `-0.0102` n `26`; metal avg `0.0136` n `20`; unknown avg `1.1329` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
