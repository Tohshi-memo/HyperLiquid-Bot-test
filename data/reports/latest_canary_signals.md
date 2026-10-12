# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T22:07:31.731421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0635` n `13`; crypto_alt avg `0.4238` n `235`; crypto_major avg `0.1733` n `8`; equity avg `0.0672` n `151`; fx avg `0.0034` n `6`; index avg `0.0281` n `26`; metal avg `0.0364` n `20`; unknown avg `0.2358` n `1117`
- 1h: commodity avg `0.1138` n `13`; crypto_alt avg `-0.6467` n `235`; crypto_major avg `-0.4223` n `8`; equity avg `-0.0656` n `151`; fx avg `0.0079` n `6`; index avg `0.0314` n `26`; metal avg `0.0219` n `20`; unknown avg `0.8171` n `1095`
- 4h: commodity avg `-0.0988` n `13`; crypto_alt avg `-0.6061` n `235`; crypto_major avg `-0.3056` n `8`; equity avg `0.0324` n `151`; fx avg `-0.0022` n `6`; index avg `0.0176` n `26`; metal avg `0.053` n `20`; unknown avg `0.9855` n `1060`
- 24h: commodity avg `0.3727` n `13`; crypto_alt avg `-3.3983` n `235`; crypto_major avg `-2.0573` n `8`; equity avg `-3.4221` n `151`; fx avg `-0.1406` n `6`; index avg `-0.3325` n `26`; metal avg `-0.0879` n `20`; unknown avg `0.1231` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2036`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1736`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1081`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0917`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0868`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0759`, n `666`, weak_sample_signal
