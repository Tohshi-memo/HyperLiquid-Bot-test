# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T08:07:28.310690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `13`; crypto_alt avg `-0.1141` n `236`; crypto_major avg `0.0269` n `8`; equity avg `0.0631` n `151`; fx avg `-0.0141` n `6`; index avg `0.022` n `26`; metal avg `-0.044` n `20`; unknown avg `-0.0942` n `1078`
- 1h: commodity avg `-0.0196` n `13`; crypto_alt avg `-0.252` n `236`; crypto_major avg `0.0261` n `8`; equity avg `-0.0396` n `151`; fx avg `0.0157` n `6`; index avg `-0.0013` n `26`; metal avg `0.001` n `20`; unknown avg `0.0475` n `1078`
- 4h: commodity avg `0.072` n `13`; crypto_alt avg `0.6724` n `236`; crypto_major avg `0.5256` n `8`; equity avg `-0.4716` n `151`; fx avg `-0.0946` n `6`; index avg `-0.0909` n `26`; metal avg `-0.0695` n `20`; unknown avg `8.7565` n `1056`
- 24h: commodity avg `0.1503` n `13`; crypto_alt avg `4.1784` n `236`; crypto_major avg `1.919` n `8`; equity avg `2.6467` n `151`; fx avg `0.0125` n `6`; index avg `0.3394` n `26`; metal avg `0.3468` n `20`; unknown avg `27.9725` n `864`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0974`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0942`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0914`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
