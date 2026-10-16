# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T16:22:34.150902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1197` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1421` n `13`; crypto_alt avg `0.1859` n `236`; crypto_major avg `0.352` n `8`; equity avg `0.1098` n `151`; fx avg `0.0073` n `6`; index avg `0.0314` n `26`; metal avg `0.0228` n `20`; unknown avg `0.8729` n `1174`
- 1h: commodity avg `0.4002` n `13`; crypto_alt avg `0.3759` n `236`; crypto_major avg `0.2729` n `8`; equity avg `-0.0025` n `151`; fx avg `-0.0148` n `6`; index avg `0.0005` n `26`; metal avg `-0.0732` n `20`; unknown avg `0.8899` n `1140`
- 4h: commodity avg `0.1501` n `13`; crypto_alt avg `-1.6067` n `236`; crypto_major avg `-1.4405` n `8`; equity avg `-2.2082` n `151`; fx avg `-0.0018` n `6`; index avg `-0.3208` n `26`; metal avg `-0.1527` n `20`; unknown avg `0.968` n `996`
- 24h: commodity avg `-0.1662` n `13`; crypto_alt avg `-0.3198` n `236`; crypto_major avg `-0.8329` n `8`; equity avg `-1.1385` n `151`; fx avg `0.0145` n `6`; index avg `-0.2059` n `26`; metal avg `0.1186` n `20`; unknown avg `-0.0664` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1197`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0946`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0842`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
