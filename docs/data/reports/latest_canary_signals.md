# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T12:52:29.082187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `0.0613` n `235`; crypto_major avg `-0.0313` n `8`; equity avg `0.0136` n `150`; fx avg `0.0149` n `6`; index avg `0.0065` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.0672` n `1093`
- 1h: commodity avg `0.0475` n `13`; crypto_alt avg `0.2554` n `235`; crypto_major avg `-0.0773` n `8`; equity avg `0.053` n `150`; fx avg `0.0029` n `6`; index avg `0.0094` n `26`; metal avg `0.0057` n `20`; unknown avg `0.4751` n `1085`
- 4h: commodity avg `-0.0262` n `13`; crypto_alt avg `-0.0617` n `235`; crypto_major avg `0.0457` n `8`; equity avg `0.1082` n `150`; fx avg `0.0267` n `6`; index avg `0.0078` n `26`; metal avg `0.0004` n `20`; unknown avg `0.5301` n `1085`
- 24h: commodity avg `0.3184` n `13`; crypto_alt avg `1.2182` n `235`; crypto_major avg `0.0264` n `8`; equity avg `0.1619` n `150`; fx avg `0.0196` n `6`; index avg `0.0057` n `26`; metal avg `0.0101` n `20`; unknown avg `0.57` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
