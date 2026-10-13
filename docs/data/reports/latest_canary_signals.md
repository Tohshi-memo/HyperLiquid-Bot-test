# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T07:22:31.389542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0374` n `13`; crypto_alt avg `0.0714` n `235`; crypto_major avg `0.1349` n `8`; equity avg `0.0905` n `151`; fx avg `0.0032` n `6`; index avg `0.0141` n `26`; metal avg `0.0661` n `20`; unknown avg `0.1201` n `1135`
- 1h: commodity avg `-0.0573` n `13`; crypto_alt avg `-0.0535` n `235`; crypto_major avg `0.0089` n `8`; equity avg `-0.1023` n `151`; fx avg `-0.027` n `6`; index avg `0.0132` n `26`; metal avg `0.0975` n `20`; unknown avg `1.1939` n `1133`
- 4h: commodity avg `-0.1013` n `13`; crypto_alt avg `1.6201` n `235`; crypto_major avg `1.0435` n `8`; equity avg `0.275` n `151`; fx avg `-0.0037` n `6`; index avg `0.1018` n `26`; metal avg `0.1879` n `20`; unknown avg `1.104` n `1075`
- 24h: commodity avg `0.3505` n `13`; crypto_alt avg `-3.7428` n `235`; crypto_major avg `-2.4117` n `8`; equity avg `-3.6268` n `151`; fx avg `0.042` n `6`; index avg `-0.47` n `26`; metal avg `0.0275` n `20`; unknown avg `0.4579` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1965`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1785`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1557`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1333`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0874`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0819`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.081`, n `666`, weak_sample_signal
