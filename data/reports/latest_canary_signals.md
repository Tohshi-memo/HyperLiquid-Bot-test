# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T11:37:40.540892+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0934` n `12`; crypto_alt avg `-0.0651` n `230`; crypto_major avg `-0.0648` n `8`; equity avg `0.0443` n `108`; fx avg `-0.003` n `6`; index avg `0.0334` n `25`; metal avg `0.0823` n `20`; unknown avg `0.0103` n `782`
- 1h: commodity avg `-0.0918` n `12`; crypto_alt avg `-0.1085` n `230`; crypto_major avg `-0.1104` n `8`; equity avg `0.0571` n `108`; fx avg `-0.0079` n `6`; index avg `0.0691` n `25`; metal avg `0.2514` n `20`; unknown avg `-0.0012` n `782`
- 4h: commodity avg `-0.075` n `12`; crypto_alt avg `-0.0919` n `230`; crypto_major avg `0.0931` n `8`; equity avg `-0.312` n `108`; fx avg `0.0152` n `6`; index avg `0.0235` n `25`; metal avg `0.0156` n `20`; unknown avg `0.7004` n `781`
- 24h: commodity avg `-0.8642` n `12`; crypto_alt avg `0.6165` n `230`; crypto_major avg `0.461` n `8`; equity avg `2.0258` n `108`; fx avg `0.0351` n `6`; index avg `0.5891` n `25`; metal avg `0.9852` n `20`; unknown avg `0.094` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
