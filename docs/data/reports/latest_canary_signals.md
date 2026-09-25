# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T07:37:42.326143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `-0.2187` n `234`; crypto_major avg `-0.1689` n `8`; equity avg `-0.048` n `141`; fx avg `0.0154` n `6`; index avg `-0.0165` n `26`; metal avg `0.0119` n `20`; unknown avg `-0.1596` n `946`
- 1h: commodity avg `0.1115` n `12`; crypto_alt avg `0.1408` n `234`; crypto_major avg `0.1072` n `8`; equity avg `-0.0614` n `141`; fx avg `0.0115` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0408` n `20`; unknown avg `1.5367` n `944`
- 4h: commodity avg `0.051` n `12`; crypto_alt avg `0.4501` n `234`; crypto_major avg `-0.0624` n `8`; equity avg `0.2754` n `141`; fx avg `-0.0159` n `6`; index avg `0.0655` n `26`; metal avg `-0.0149` n `20`; unknown avg `0.1319` n `906`
- 24h: commodity avg `0.4306` n `12`; crypto_alt avg `1.4878` n `234`; crypto_major avg `-0.3297` n `8`; equity avg `0.8211` n `141`; fx avg `-0.1544` n `6`; index avg `0.1248` n `26`; metal avg `-0.2616` n `20`; unknown avg `11.3359` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
