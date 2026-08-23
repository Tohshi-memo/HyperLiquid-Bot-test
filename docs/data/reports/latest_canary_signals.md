# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T04:22:48.529409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0771` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `0.033` n `230`; crypto_major avg `-0.1164` n `8`; equity avg `0.0083` n `121`; fx avg `0.0028` n `6`; index avg `0.001` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0058` n `794`
- 1h: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.74` n `230`; crypto_major avg `-0.5125` n `8`; equity avg `-0.0478` n `121`; fx avg `-0.0068` n `6`; index avg `0.0032` n `25`; metal avg `-0.0124` n `20`; unknown avg `-0.2068` n `794`
- 4h: commodity avg `-0.0379` n `12`; crypto_alt avg `-2.2739` n `230`; crypto_major avg `-1.0572` n `8`; equity avg `0.0284` n `121`; fx avg `0.0124` n `6`; index avg `0.0199` n `25`; metal avg `0.0118` n `20`; unknown avg `2.1904` n `794`
- 24h: commodity avg `0.0351` n `12`; crypto_alt avg `-7.9842` n `230`; crypto_major avg `-3.8681` n `8`; equity avg `-0.281` n `121`; fx avg `0.0867` n `6`; index avg `-0.0173` n `25`; metal avg `-0.0045` n `20`; unknown avg `1.8955` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
