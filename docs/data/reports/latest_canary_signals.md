# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T11:37:30.173477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0483` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.2986` n `235`; crypto_major avg `-0.1516` n `8`; equity avg `0.0355` n `151`; fx avg `0.0005` n `6`; index avg `0.0033` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.3447` n `1135`
- 1h: commodity avg `0.1616` n `13`; crypto_alt avg `-0.3916` n `235`; crypto_major avg `0.1423` n `8`; equity avg `-0.294` n `151`; fx avg `0.0055` n `6`; index avg `-0.031` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.3698` n `1133`
- 4h: commodity avg `0.0074` n `13`; crypto_alt avg `-2.0697` n `235`; crypto_major avg `-1.0523` n `8`; equity avg `-0.072` n `151`; fx avg `-0.0225` n `6`; index avg `-0.004` n `26`; metal avg `-0.051` n `20`; unknown avg `0.0719` n `1117`
- 24h: commodity avg `-0.0272` n `13`; crypto_alt avg `-4.3316` n `235`; crypto_major avg `-2.1984` n `8`; equity avg `-2.9922` n `151`; fx avg `0.0583` n `6`; index avg `-0.3635` n `26`; metal avg `-0.0188` n `20`; unknown avg `0.1117` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1703`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1681`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1535`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1458`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
