# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T04:22:30.852799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `12`; crypto_alt avg `0.0888` n `234`; crypto_major avg `0.0878` n `8`; equity avg `0.0108` n `141`; fx avg `0.0` n `6`; index avg `0.0026` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.0474` n `961`
- 1h: commodity avg `0.0195` n `12`; crypto_alt avg `-0.1152` n `234`; crypto_major avg `0.0558` n `8`; equity avg `0.0229` n `141`; fx avg `0.0014` n `6`; index avg `0.0067` n `26`; metal avg `-0.003` n `20`; unknown avg `23.6636` n `953`
- 4h: commodity avg `0.0076` n `12`; crypto_alt avg `-0.11` n `234`; crypto_major avg `0.1327` n `8`; equity avg `0.0528` n `141`; fx avg `-0.0094` n `6`; index avg `0.0038` n `26`; metal avg `-0.0122` n `20`; unknown avg `-0.0161` n `947`
- 24h: commodity avg `0.0057` n `12`; crypto_alt avg `0.5399` n `234`; crypto_major avg `-0.2365` n `8`; equity avg `0.2666` n `141`; fx avg `0.0103` n `6`; index avg `-0.0048` n `26`; metal avg `-0.009` n `20`; unknown avg `4.8394` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
