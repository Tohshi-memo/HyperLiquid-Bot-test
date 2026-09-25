# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T03:52:30.795560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.0062` n `234`; crypto_major avg `-0.0697` n `8`; equity avg `-0.0607` n `141`; fx avg `-0.0099` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0172` n `20`; unknown avg `0.9128` n `946`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `0.0226` n `234`; crypto_major avg `-0.0631` n `8`; equity avg `0.1003` n `141`; fx avg `-0.0301` n `6`; index avg `0.012` n `26`; metal avg `-0.0319` n `20`; unknown avg `0.9743` n `944`
- 4h: commodity avg `-0.1604` n `12`; crypto_alt avg `-0.8302` n `234`; crypto_major avg `-0.4649` n `8`; equity avg `0.3364` n `141`; fx avg `-0.1542` n `6`; index avg `0.0931` n `26`; metal avg `-0.0585` n `20`; unknown avg `0.5247` n `938`
- 24h: commodity avg `0.5074` n `12`; crypto_alt avg `2.3848` n `234`; crypto_major avg `0.899` n `8`; equity avg `0.3852` n `141`; fx avg `-0.1441` n `6`; index avg `0.0318` n `26`; metal avg `-0.1305` n `20`; unknown avg `17.91` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
