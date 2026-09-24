# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T11:07:34.341114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0752` n `12`; crypto_alt avg `0.2845` n `234`; crypto_major avg `0.1328` n `8`; equity avg `0.0409` n `141`; fx avg `-0.0016` n `6`; index avg `-0.0108` n `26`; metal avg `-0.0224` n `20`; unknown avg `-0.1226` n `943`
- 1h: commodity avg `-0.0909` n `12`; crypto_alt avg `0.6213` n `234`; crypto_major avg `0.5427` n `8`; equity avg `0.3453` n `141`; fx avg `0.0012` n `6`; index avg `0.0521` n `26`; metal avg `0.0178` n `20`; unknown avg `0.4999` n `943`
- 4h: commodity avg `0.1739` n `12`; crypto_alt avg `-1.1957` n `234`; crypto_major avg `-1.0286` n `8`; equity avg `-0.3563` n `141`; fx avg `0.0011` n `6`; index avg `-0.052` n `26`; metal avg `-0.2026` n `20`; unknown avg `0.3459` n `937`
- 24h: commodity avg `0.6344` n `12`; crypto_alt avg `-4.7112` n `234`; crypto_major avg `-3.8893` n `8`; equity avg `-2.1983` n `141`; fx avg `0.0176` n `6`; index avg `-0.4358` n `26`; metal avg `-0.4998` n `20`; unknown avg `587.3267` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
