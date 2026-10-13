# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T10:52:29.629433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.5057` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.1506` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0381` n `13`; crypto_alt avg `-0.0051` n `235`; crypto_major avg `0.0305` n `8`; equity avg `1.1987` n `151`; fx avg `0.0037` n `6`; index avg `-0.0117` n `26`; metal avg `-0.0342` n `20`; unknown avg `1.0496` n `1135`
- 1h: commodity avg `-0.0309` n `13`; crypto_alt avg `-0.4879` n `235`; crypto_major avg `-0.3951` n `8`; equity avg `1.0695` n `151`; fx avg `0.0377` n `6`; index avg `-0.0434` n `26`; metal avg `-0.0544` n `20`; unknown avg `0.2504` n `1133`
- 4h: commodity avg `-0.1589` n `13`; crypto_alt avg `-1.8354` n `235`; crypto_major avg `-1.1412` n `8`; equity avg `1.3645` n `151`; fx avg `0.0008` n `6`; index avg `0.0094` n `26`; metal avg `-0.0397` n `20`; unknown avg `1.3814` n `1117`
- 24h: commodity avg `-0.0478` n `13`; crypto_alt avg `-4.5757` n `235`; crypto_major avg `-2.6869` n `8`; equity avg `-1.7348` n `151`; fx avg `0.0641` n `6`; index avg `-0.3647` n `26`; metal avg `-0.0511` n `20`; unknown avg `0.2814` n `973`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1737`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1669`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1626`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1454`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0729`, n `666`, weak_sample_signal
