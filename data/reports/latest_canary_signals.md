# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T08:52:32.242187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0966` n `12`; crypto_alt avg `0.0045` n `234`; crypto_major avg `-0.0698` n `8`; equity avg `0.0397` n `141`; fx avg `-0.0001` n `6`; index avg `0.0203` n `26`; metal avg `0.0645` n `20`; unknown avg `1.5779` n `946`
- 1h: commodity avg `-0.2137` n `12`; crypto_alt avg `1.0187` n `234`; crypto_major avg `0.5647` n `8`; equity avg `0.2692` n `141`; fx avg `-0.0005` n `6`; index avg `0.0579` n `26`; metal avg `0.191` n `20`; unknown avg `1.9789` n `926`
- 4h: commodity avg `-0.1491` n `12`; crypto_alt avg `1.2829` n `234`; crypto_major avg `0.5256` n `8`; equity avg `0.5442` n `141`; fx avg `-0.0288` n `6`; index avg `0.1251` n `26`; metal avg `0.2135` n `20`; unknown avg `2.92` n `904`
- 24h: commodity avg `-0.1516` n `12`; crypto_alt avg `4.134` n `234`; crypto_major avg `1.8686` n `8`; equity avg `2.161` n `141`; fx avg `-0.2073` n `6`; index avg `0.3324` n `26`; metal avg `0.1531` n `20`; unknown avg `16.9412` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
