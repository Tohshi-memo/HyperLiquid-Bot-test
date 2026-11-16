# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T09:52:27.689874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1457` n `13`; crypto_alt avg `-0.2384` n `239`; crypto_major avg `-0.1206` n `8`; equity avg `-0.2717` n `162`; fx avg `-0.0025` n `6`; index avg `-0.0373` n `27`; metal avg `-0.0506` n `20`; unknown avg `158.1536` n `1265`
- 1h: commodity avg `-0.0166` n `13`; crypto_alt avg `-0.2999` n `239`; crypto_major avg `-0.3731` n `8`; equity avg `-0.5272` n `162`; fx avg `-0.0518` n `6`; index avg `-0.0551` n `27`; metal avg `-0.1057` n `20`; unknown avg `8.4793` n `1259`
- 4h: commodity avg `-0.1339` n `13`; crypto_alt avg `-0.4463` n `239`; crypto_major avg `-0.3665` n `8`; equity avg `-0.1961` n `162`; fx avg `-0.0393` n `6`; index avg `0.0331` n `27`; metal avg `-0.0173` n `20`; unknown avg `14.4021` n `1077`
- 24h: commodity avg `-0.3587` n `13`; crypto_alt avg `-1.4197` n `239`; crypto_major avg `-1.3239` n `8`; equity avg `-0.9736` n `162`; fx avg `-0.0886` n `6`; index avg `-0.057` n `27`; metal avg `-0.1055` n `20`; unknown avg `14.7358` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
