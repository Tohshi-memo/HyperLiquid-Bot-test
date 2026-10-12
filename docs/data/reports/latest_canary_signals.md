# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T03:52:24.721656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `13`; crypto_alt avg `-0.1032` n `235`; crypto_major avg `-0.0672` n `8`; equity avg `-0.0451` n `151`; fx avg `0.0097` n `6`; index avg `-0.0086` n `26`; metal avg `0.0117` n `20`; unknown avg `1.0649` n `1133`
- 1h: commodity avg `0.0452` n `13`; crypto_alt avg `-0.087` n `235`; crypto_major avg `-0.1504` n `8`; equity avg `-0.1125` n `151`; fx avg `-0.0191` n `6`; index avg `-0.025` n `26`; metal avg `-0.0199` n `20`; unknown avg `0.0175` n `1131`
- 4h: commodity avg `-0.1245` n `13`; crypto_alt avg `-0.0681` n `235`; crypto_major avg `0.0439` n `8`; equity avg `-0.7121` n `151`; fx avg `-0.0844` n `6`; index avg `-0.0535` n `26`; metal avg `0.0966` n `20`; unknown avg `0.339` n `1097`
- 24h: commodity avg `-0.4621` n `13`; crypto_alt avg `3.2496` n `235`; crypto_major avg `1.4609` n `8`; equity avg `-0.2073` n `151`; fx avg `-0.0696` n `6`; index avg `0.019` n `26`; metal avg `0.1627` n `20`; unknown avg `1.1113` n `928`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
