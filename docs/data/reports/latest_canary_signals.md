# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T04:37:27.847313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0229` n `12`; crypto_alt avg `-0.2725` n `234`; crypto_major avg `-0.1319` n `8`; equity avg `-0.0166` n `141`; fx avg `0.0081` n `6`; index avg `-0.013` n `26`; metal avg `-0.0017` n `20`; unknown avg `27.9363` n `961`
- 1h: commodity avg `0.0149` n `12`; crypto_alt avg `-0.2028` n `234`; crypto_major avg `-0.2642` n `8`; equity avg `-0.0168` n `141`; fx avg `0.001` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0049` n `20`; unknown avg `17.8069` n `953`
- 4h: commodity avg `-0.2745` n `12`; crypto_alt avg `-0.1391` n `234`; crypto_major avg `-0.087` n `8`; equity avg `0.0597` n `141`; fx avg `0.011` n `6`; index avg `0.0405` n `26`; metal avg `0.0215` n `20`; unknown avg `9.9855` n `952`
- 24h: commodity avg `0.0348` n `12`; crypto_alt avg `2.7153` n `234`; crypto_major avg `0.7956` n `8`; equity avg `-0.3946` n `141`; fx avg `-0.1107` n `6`; index avg `0.1243` n `26`; metal avg `0.236` n `20`; unknown avg `1126.579` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
