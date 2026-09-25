# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T07:22:32.084380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.098` n `12`; crypto_alt avg `0.1838` n `234`; crypto_major avg `0.1443` n `8`; equity avg `0.0081` n `141`; fx avg `0.0028` n `6`; index avg `0.0054` n `26`; metal avg `-0.0512` n `20`; unknown avg `0.0139` n `946`
- 1h: commodity avg `0.1203` n `12`; crypto_alt avg `-0.0186` n `234`; crypto_major avg `-0.0274` n `8`; equity avg `-0.0544` n `141`; fx avg `-0.0005` n `6`; index avg `0.0056` n `26`; metal avg `-0.0697` n `20`; unknown avg `0.4585` n `944`
- 4h: commodity avg `0.1451` n `12`; crypto_alt avg `0.7941` n `234`; crypto_major avg `0.1349` n `8`; equity avg `0.3149` n `141`; fx avg `-0.0419` n `6`; index avg `0.0734` n `26`; metal avg `-0.0887` n `20`; unknown avg `0.2456` n `906`
- 24h: commodity avg `0.462` n `12`; crypto_alt avg `2.1029` n `234`; crypto_major avg `0.4309` n `8`; equity avg `1.0764` n `141`; fx avg `-0.1949` n `6`; index avg `0.1645` n `26`; metal avg `-0.2242` n `20`; unknown avg `12.9035` n `799`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
