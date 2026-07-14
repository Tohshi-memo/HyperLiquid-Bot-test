# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T20:52:25.083068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.97` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0521` n `12`; crypto_alt avg `0.0377` n `230`; crypto_major avg `0.0177` n `8`; equity avg `-0.0067` n `92`; fx avg `0.0048` n `6`; index avg `0.0016` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.2103` n `768`
- 1h: commodity avg `0.0271` n `12`; crypto_alt avg `-0.087` n `230`; crypto_major avg `-0.1725` n `8`; equity avg `0.0516` n `92`; fx avg `0.0092` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0232` n `20`; unknown avg `0.0653` n `768`
- 4h: commodity avg `0.1511` n `12`; crypto_alt avg `-0.4875` n `230`; crypto_major avg `-0.122` n `8`; equity avg `0.1264` n `92`; fx avg `0.002` n `6`; index avg `-0.014` n `25`; metal avg `-0.0606` n `20`; unknown avg `0.2006` n `766`
- 24h: commodity avg `0.3168` n `12`; crypto_alt avg `1.9419` n `230`; crypto_major avg `3.4653` n `8`; equity avg `1.4369` n `92`; fx avg `0.0028` n `6`; index avg `0.4364` n `25`; metal avg `0.5703` n `20`; unknown avg `0.2078` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
