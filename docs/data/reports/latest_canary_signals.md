# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T07:37:26.303644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `0.1125` n `235`; crypto_major avg `0.1655` n `8`; equity avg `0.0057` n `151`; fx avg `0.0159` n `6`; index avg `0.0003` n `26`; metal avg `-0.0207` n `20`; unknown avg `0.2714` n `1135`
- 1h: commodity avg `-0.046` n `13`; crypto_alt avg `-0.1165` n `235`; crypto_major avg `0.0352` n `8`; equity avg `-0.0761` n `151`; fx avg `0.0015` n `6`; index avg `0.0297` n `26`; metal avg `0.1055` n `20`; unknown avg `0.2789` n `1133`
- 4h: commodity avg `-0.1138` n `13`; crypto_alt avg `1.2223` n `235`; crypto_major avg `0.7273` n `8`; equity avg `0.0572` n `151`; fx avg `0.0113` n `6`; index avg `0.0677` n `26`; metal avg `0.159` n `20`; unknown avg `1.2908` n `1107`
- 24h: commodity avg `0.4581` n `13`; crypto_alt avg `-3.5665` n `235`; crypto_major avg `-2.1098` n `8`; equity avg `-3.606` n `151`; fx avg `0.0545` n `6`; index avg `-0.4746` n `26`; metal avg `-0.0492` n `20`; unknown avg `0.5762` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1965`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1777`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1554`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1333`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0873`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0816`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `666`, weak_sample_signal
