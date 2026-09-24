# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T12:52:44.598134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0554` n `12`; crypto_alt avg `0.2291` n `234`; crypto_major avg `0.1896` n `8`; equity avg `0.1534` n `141`; fx avg `-0.0077` n `6`; index avg `0.0225` n `26`; metal avg `0.0404` n `20`; unknown avg `1.4418` n `945`
- 1h: commodity avg `-0.0811` n `12`; crypto_alt avg `0.3765` n `234`; crypto_major avg `0.2771` n `8`; equity avg `-0.0543` n `141`; fx avg `-0.0221` n `6`; index avg `0.0246` n `26`; metal avg `0.0315` n `20`; unknown avg `2.7555` n `937`
- 4h: commodity avg `-0.2615` n `12`; crypto_alt avg `-0.1833` n `234`; crypto_major avg `-0.2553` n `8`; equity avg `0.2147` n `141`; fx avg `-0.0388` n `6`; index avg `0.0428` n `26`; metal avg `0.0173` n `20`; unknown avg `1.7574` n `937`
- 24h: commodity avg `0.363` n `12`; crypto_alt avg `-3.9279` n `234`; crypto_major avg `-3.0971` n `8`; equity avg `-2.1582` n `141`; fx avg `-0.0074` n `6`; index avg `-0.3938` n `26`; metal avg `-0.2546` n `20`; unknown avg `586.1964` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
