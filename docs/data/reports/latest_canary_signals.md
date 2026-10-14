# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T15:07:27.018245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8149` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0617` n `13`; crypto_alt avg `-0.1074` n `235`; crypto_major avg `-0.0016` n `8`; equity avg `-0.3415` n `151`; fx avg `-0.013` n `6`; index avg `-0.0416` n `26`; metal avg `-0.0415` n `20`; unknown avg `-0.0747` n `1135`
- 1h: commodity avg `0.0041` n `13`; crypto_alt avg `-0.5187` n `235`; crypto_major avg `-0.5946` n `8`; equity avg `-0.4678` n `151`; fx avg `-0.005` n `6`; index avg `-0.0585` n `26`; metal avg `-0.1251` n `20`; unknown avg `0.0141` n `1110`
- 4h: commodity avg `-0.2221` n `13`; crypto_alt avg `-2.1244` n `235`; crypto_major avg `-2.113` n `8`; equity avg `-2.1822` n `151`; fx avg `-0.1272` n `6`; index avg `-0.2981` n `26`; metal avg `-0.627` n `20`; unknown avg `2.7893` n `1102`
- 24h: commodity avg `0.1928` n `13`; crypto_alt avg `-2.8635` n `235`; crypto_major avg `-2.4026` n `8`; equity avg `-2.3592` n `151`; fx avg `-0.1594` n `6`; index avg `-0.2813` n `26`; metal avg `-0.8258` n `20`; unknown avg `1263.1762` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0917`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0781`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0694`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0578`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
