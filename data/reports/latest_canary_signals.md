# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T13:07:35.859111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0461` n `12`; crypto_alt avg `-0.0562` n `230`; crypto_major avg `-0.016` n `8`; equity avg `0.0635` n `107`; fx avg `0.0052` n `6`; index avg `0.0263` n `25`; metal avg `-0.1797` n `20`; unknown avg `0.0856` n `781`
- 1h: commodity avg `-0.045` n `12`; crypto_alt avg `-0.0801` n `230`; crypto_major avg `0.0538` n `8`; equity avg `-0.1372` n `107`; fx avg `0.0306` n `6`; index avg `0.013` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.047` n `781`
- 4h: commodity avg `-1.0615` n `12`; crypto_alt avg `-0.1188` n `230`; crypto_major avg `0.6956` n `8`; equity avg `0.9253` n `107`; fx avg `-0.0874` n `6`; index avg `0.2182` n `25`; metal avg `0.4209` n `20`; unknown avg `0.1879` n `781`
- 24h: commodity avg `-0.5017` n `12`; crypto_alt avg `0.8651` n `230`; crypto_major avg `1.7584` n `8`; equity avg `5.1269` n `107`; fx avg `0.0211` n `6`; index avg `0.6335` n `25`; metal avg `0.9463` n `20`; unknown avg `0.9314` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
