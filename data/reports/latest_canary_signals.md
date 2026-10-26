# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T21:22:34.565143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `0.0593` n `237`; crypto_major avg `0.1397` n `8`; equity avg `0.0417` n `154`; fx avg `-0.0031` n `6`; index avg `-0.0004` n `27`; metal avg `-0.0037` n `20`; unknown avg `0.1798` n `1236`
- 1h: commodity avg `-0.0214` n `13`; crypto_alt avg `-0.2207` n `237`; crypto_major avg `-0.0899` n `8`; equity avg `0.1047` n `154`; fx avg `-0.0118` n `6`; index avg `0.0141` n `27`; metal avg `0.0132` n `20`; unknown avg `11.1297` n `1220`
- 4h: commodity avg `-0.2108` n `13`; crypto_alt avg `-1.1512` n `237`; crypto_major avg `-0.7966` n `8`; equity avg `-0.4549` n `154`; fx avg `-0.0388` n `6`; index avg `-0.0761` n `27`; metal avg `-0.1237` n `20`; unknown avg `9.1536` n `1134`
- 24h: commodity avg `-0.3815` n `13`; crypto_alt avg `-0.5911` n `237`; crypto_major avg `-0.2938` n `8`; equity avg `0.5571` n `153`; fx avg `-0.0201` n `6`; index avg `-0.0932` n `27`; metal avg `0.0119` n `20`; unknown avg `703.0398` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
