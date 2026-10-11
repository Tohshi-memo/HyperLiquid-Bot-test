# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T13:52:29.641322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `13`; crypto_alt avg `-0.0331` n `235`; crypto_major avg `-0.071` n `8`; equity avg `-0.0195` n `150`; fx avg `0.001` n `6`; index avg `0.0162` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.5226` n `1134`
- 1h: commodity avg `-0.025` n `13`; crypto_alt avg `0.1658` n `235`; crypto_major avg `-0.0048` n `8`; equity avg `-0.0129` n `150`; fx avg `-0.0244` n `6`; index avg `0.0031` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.6796` n `1083`
- 4h: commodity avg `-0.0499` n `13`; crypto_alt avg `0.2905` n `235`; crypto_major avg `0.0941` n `8`; equity avg `0.0867` n `150`; fx avg `0.0018` n `6`; index avg `0.0095` n `26`; metal avg `0.0027` n `20`; unknown avg `1.1057` n `1053`
- 24h: commodity avg `0.3048` n `13`; crypto_alt avg `1.175` n `235`; crypto_major avg `-0.0748` n `8`; equity avg `0.134` n `150`; fx avg `0.003` n `6`; index avg `0.0133` n `26`; metal avg `0.0016` n `20`; unknown avg `1.0553` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
