# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T11:37:29.183231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0929` n `232`; crypto_major avg `0.0064` n `8`; equity avg `0.0301` n `133`; fx avg `-0.0077` n `6`; index avg `0.0024` n `26`; metal avg `0.0014` n `20`; unknown avg `0.2438` n `793`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.4613` n `232`; crypto_major avg `0.2678` n `8`; equity avg `0.0065` n `133`; fx avg `-0.0012` n `6`; index avg `0.0135` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.2271` n `791`
- 4h: commodity avg `-0.095` n `12`; crypto_alt avg `1.1322` n `232`; crypto_major avg `0.7233` n `8`; equity avg `0.4046` n `133`; fx avg `-0.0404` n `6`; index avg `0.0595` n `26`; metal avg `-0.0489` n `20`; unknown avg `0.0847` n `785`
- 24h: commodity avg `-0.534` n `12`; crypto_alt avg `2.7454` n `232`; crypto_major avg `4.0043` n `8`; equity avg `2.3247` n `133`; fx avg `-0.0017` n `6`; index avg `0.4256` n `26`; metal avg `0.4287` n `20`; unknown avg `2.0956` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
