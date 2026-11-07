# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T14:52:25.034483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `0.0216` n `239`; crypto_major avg `-0.0388` n `8`; equity avg `-0.0129` n `158`; fx avg `-0.009` n `6`; index avg `0.0004` n `27`; metal avg `0.0037` n `20`; unknown avg `0.0135` n `1261`
- 1h: commodity avg `0.0056` n `13`; crypto_alt avg `-0.0016` n `239`; crypto_major avg `0.0483` n `8`; equity avg `-0.0498` n `158`; fx avg `-0.0222` n `6`; index avg `-0.0011` n `27`; metal avg `0.0043` n `20`; unknown avg `0.1407` n `1255`
- 4h: commodity avg `0.0136` n `13`; crypto_alt avg `0.1169` n `239`; crypto_major avg `-0.0297` n `8`; equity avg `0.0196` n `158`; fx avg `0.0191` n `6`; index avg `0.0134` n `27`; metal avg `0.0031` n `20`; unknown avg `-0.1412` n `1249`
- 24h: commodity avg `0.1515` n `13`; crypto_alt avg `-1.6569` n `239`; crypto_major avg `-0.3215` n `8`; equity avg `-0.4796` n `158`; fx avg `-0.0109` n `6`; index avg `-0.0722` n `27`; metal avg `0.0519` n `20`; unknown avg `0.1117` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
