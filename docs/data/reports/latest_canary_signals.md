# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T07:52:26.540543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0795` n `13`; crypto_alt avg `-0.0109` n `235`; crypto_major avg `-0.0313` n `8`; equity avg `-0.0349` n `151`; fx avg `-0.0139` n `6`; index avg `0.0004` n `26`; metal avg `0.0102` n `20`; unknown avg `4.0708` n `1135`
- 1h: commodity avg `-0.0142` n `13`; crypto_alt avg `-0.0141` n `235`; crypto_major avg `0.0289` n `8`; equity avg `0.0354` n `151`; fx avg `-0.0331` n `6`; index avg `-0.0161` n `26`; metal avg `-0.0539` n `20`; unknown avg `3.7994` n `1133`
- 4h: commodity avg `-0.1163` n `13`; crypto_alt avg `-0.7028` n `235`; crypto_major avg `-0.4431` n `8`; equity avg `-0.6982` n `151`; fx avg `-0.035` n `6`; index avg `-0.0963` n `26`; metal avg `-0.1315` n `20`; unknown avg `1.4759` n `1111`
- 24h: commodity avg `1.0112` n `13`; crypto_alt avg `-1.2095` n `235`; crypto_major avg `-0.7622` n `8`; equity avg `-0.1448` n `151`; fx avg `-0.0289` n `6`; index avg `-0.0206` n `26`; metal avg `-0.4735` n `20`; unknown avg `0.558` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.155`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1351`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0717`, n `666`, weak_sample_signal
