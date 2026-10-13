# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T01:22:23.516260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8705` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7272` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `0.9431` n `235`; crypto_major avg `0.6956` n `8`; equity avg `0.0224` n `151`; fx avg `-0.0033` n `6`; index avg `-0.0287` n `26`; metal avg `0.0002` n `20`; unknown avg `0.8597` n `1135`
- 1h: commodity avg `-0.0078` n `13`; crypto_alt avg `0.4047` n `235`; crypto_major avg `0.8665` n `8`; equity avg `-0.2146` n `151`; fx avg `0.0432` n `6`; index avg `-0.0842` n `26`; metal avg `-0.005` n `20`; unknown avg `1.3044` n `1133`
- 4h: commodity avg `-0.0157` n `13`; crypto_alt avg `-2.8546` n `235`; crypto_major avg `-1.9814` n `8`; equity avg `-1.2911` n `151`; fx avg `0.047` n `6`; index avg `-0.2542` n `26`; metal avg `-0.1109` n `20`; unknown avg `4.5979` n `1089`
- 24h: commodity avg `0.7578` n `13`; crypto_alt avg `-5.6676` n `235`; crypto_major avg `-3.8594` n `8`; equity avg `-4.6657` n `151`; fx avg `-0.0543` n `6`; index avg `-0.5353` n `26`; metal avg `-0.3634` n `20`; unknown avg `0.4851` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2071`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1862`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1099`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0833`, n `666`, weak_sample_signal
