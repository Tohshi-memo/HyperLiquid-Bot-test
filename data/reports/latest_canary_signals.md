# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T15:37:27.192597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0391` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.1675` n `234`; crypto_major avg `-0.1316` n `8`; equity avg `-0.0114` n `141`; fx avg `0.0035` n `6`; index avg `0.0008` n `26`; metal avg `0.0023` n `20`; unknown avg `6.8017` n `962`
- 1h: commodity avg `-0.0729` n `12`; crypto_alt avg `-0.6262` n `234`; crypto_major avg `-0.284` n `8`; equity avg `0.0189` n `141`; fx avg `0.004` n `6`; index avg `0.0158` n `26`; metal avg `0.0003` n `20`; unknown avg `11.0571` n `960`
- 4h: commodity avg `-0.1302` n `12`; crypto_alt avg `-1.4759` n `234`; crypto_major avg `-1.0489` n `8`; equity avg `-0.087` n `141`; fx avg `0.0086` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0091` n `20`; unknown avg `17.0341` n `954`
- 24h: commodity avg `-0.0887` n `12`; crypto_alt avg `-1.7924` n `234`; crypto_major avg `-0.7552` n `8`; equity avg `0.1565` n `141`; fx avg `-0.0226` n `6`; index avg `0.0068` n `26`; metal avg `-0.016` n `20`; unknown avg `225.5474` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
