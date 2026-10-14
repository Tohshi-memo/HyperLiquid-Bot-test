# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T08:22:27.083860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0421` n `13`; crypto_alt avg `-0.3521` n `235`; crypto_major avg `-0.2509` n `8`; equity avg `0.2164` n `151`; fx avg `0.0165` n `6`; index avg `0.0318` n `26`; metal avg `0.0171` n `20`; unknown avg `390.7259` n `1135`
- 1h: commodity avg `-0.0533` n `13`; crypto_alt avg `0.369` n `235`; crypto_major avg `0.3325` n `8`; equity avg `0.3441` n `151`; fx avg `0.022` n `6`; index avg `0.0505` n `26`; metal avg `0.1033` n `20`; unknown avg `397.0689` n `1117`
- 4h: commodity avg `-0.0581` n `13`; crypto_alt avg `-0.0902` n `235`; crypto_major avg `0.1289` n `8`; equity avg `-0.3512` n `151`; fx avg `-0.0212` n `6`; index avg `-0.0622` n `26`; metal avg `-0.0393` n `20`; unknown avg `402.4718` n `1101`
- 24h: commodity avg `1.0452` n `13`; crypto_alt avg `-0.6751` n `235`; crypto_major avg `-0.3679` n `8`; equity avg `-0.1946` n `151`; fx avg `0.0074` n `6`; index avg `0.0156` n `26`; metal avg `-0.4329` n `20`; unknown avg `452.1326` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1533`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1336`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1123`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0713`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0702`, n `666`, weak_sample_signal
