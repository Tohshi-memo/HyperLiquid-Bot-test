# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T09:22:30.932379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0371` n `13`; crypto_alt avg `-0.1796` n `236`; crypto_major avg `-0.19` n `8`; equity avg `-0.0206` n `151`; fx avg `0.0034` n `6`; index avg `-0.008` n `26`; metal avg `0.0304` n `20`; unknown avg `-0.096` n `1136`
- 1h: commodity avg `0.0992` n `13`; crypto_alt avg `0.2534` n `236`; crypto_major avg `-0.0364` n `8`; equity avg `0.4259` n `151`; fx avg `0.0113` n `6`; index avg `0.044` n `26`; metal avg `0.0263` n `20`; unknown avg `0.1727` n `1134`
- 4h: commodity avg `0.0199` n `13`; crypto_alt avg `0.2676` n `236`; crypto_major avg `0.2864` n `8`; equity avg `-0.369` n `151`; fx avg `-0.0221` n `6`; index avg `-0.0147` n `26`; metal avg `0.2057` n `20`; unknown avg `4.1784` n `1092`
- 24h: commodity avg `-0.2855` n `13`; crypto_alt avg `-4.4545` n `236`; crypto_major avg `-3.1794` n `8`; equity avg `-5.7802` n `151`; fx avg `0.0831` n `6`; index avg `-0.9588` n `26`; metal avg `-0.3911` n `20`; unknown avg `1.9138` n `970`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1182`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.089`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0785`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0627`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
