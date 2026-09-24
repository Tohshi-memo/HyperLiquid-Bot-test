# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T07:22:29.451918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0857` n `12`; crypto_alt avg `-0.0109` n `234`; crypto_major avg `0.1571` n `8`; equity avg `0.0428` n `141`; fx avg `-0.007` n `6`; index avg `0.0247` n `26`; metal avg `0.0475` n `20`; unknown avg `-0.1075` n `945`
- 1h: commodity avg `-0.0708` n `12`; crypto_alt avg `-0.0585` n `234`; crypto_major avg `0.0404` n `8`; equity avg `-0.0361` n `141`; fx avg `0.0155` n `6`; index avg `0.0083` n `26`; metal avg `0.044` n `20`; unknown avg `1.4909` n `943`
- 4h: commodity avg `0.1471` n `12`; crypto_alt avg `0.4688` n `234`; crypto_major avg `0.3446` n `8`; equity avg `-0.4454` n `141`; fx avg `0.0239` n `6`; index avg `-0.0583` n `26`; metal avg `0.0636` n `20`; unknown avg `0.8138` n `921`
- 24h: commodity avg `0.4917` n `12`; crypto_alt avg `-4.2095` n `234`; crypto_major avg `-3.7739` n `8`; equity avg `-2.0788` n `140`; fx avg `0.0053` n `6`; index avg `-0.4087` n `26`; metal avg `-0.4047` n `20`; unknown avg `586.4039` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
