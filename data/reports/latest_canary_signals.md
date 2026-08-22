# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T09:52:22.823829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1035` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.4631` n `230`; crypto_major avg `-0.4883` n `8`; equity avg `-0.0366` n `121`; fx avg `0.0` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0` n `20`; unknown avg `-0.0992` n `794`
- 1h: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.4054` n `230`; crypto_major avg `-0.3875` n `8`; equity avg `-0.0273` n `121`; fx avg `0.0028` n `6`; index avg `-0.0054` n `25`; metal avg `0.005` n `20`; unknown avg `0.0422` n `794`
- 4h: commodity avg `-0.0487` n `12`; crypto_alt avg `-0.9709` n `230`; crypto_major avg `-1.1286` n `8`; equity avg `-0.1222` n `121`; fx avg `-0.0075` n `6`; index avg `-0.0251` n `25`; metal avg `-0.0171` n `20`; unknown avg `-0.0518` n `778`
- 24h: commodity avg `0.0446` n `12`; crypto_alt avg `2.6879` n `230`; crypto_major avg `2.5642` n `8`; equity avg `-0.9678` n `121`; fx avg `0.0384` n `6`; index avg `-0.0988` n `25`; metal avg `-0.1167` n `20`; unknown avg `1.3188` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
