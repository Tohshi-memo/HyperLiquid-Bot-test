# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T11:52:32.590875+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `13`; crypto_alt avg `0.0412` n `235`; crypto_major avg `0.02` n `8`; equity avg `-0.0313` n `151`; fx avg `0.0107` n `6`; index avg `-0.0011` n `26`; metal avg `0.0037` n `20`; unknown avg `1.7336` n `1136`
- 1h: commodity avg `-0.0109` n `13`; crypto_alt avg `0.0751` n `235`; crypto_major avg `0.0623` n `8`; equity avg `-0.1972` n `151`; fx avg `0.0108` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0079` n `20`; unknown avg `1.8271` n `1134`
- 4h: commodity avg `0.0782` n `13`; crypto_alt avg `-0.5244` n `235`; crypto_major avg `-0.0747` n `8`; equity avg `-0.3732` n `151`; fx avg `0.0226` n `6`; index avg `-0.0144` n `26`; metal avg `-0.0297` n `20`; unknown avg `1192.9607` n `1037`
- 24h: commodity avg `0.9541` n `13`; crypto_alt avg `0.522` n `235`; crypto_major avg `0.4054` n `8`; equity avg `-0.3177` n `151`; fx avg `0.0204` n `6`; index avg `0.0137` n `26`; metal avg `-0.4421` n `20`; unknown avg `1269.2434` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1511`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1293`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1081`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0772`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0746`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0717`, n `666`, weak_sample_signal
