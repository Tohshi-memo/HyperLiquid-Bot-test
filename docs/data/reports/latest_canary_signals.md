# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T19:22:34.193807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `0.0371` n `232`; crypto_major avg `0.1963` n `8`; equity avg `0.0052` n `133`; fx avg `-0.0068` n `6`; index avg `-0.0204` n `26`; metal avg `-0.0038` n `20`; unknown avg `4.5313` n `792`
- 1h: commodity avg `0.0598` n `12`; crypto_alt avg `0.295` n `232`; crypto_major avg `0.3997` n `8`; equity avg `-0.0581` n `133`; fx avg `0.0045` n `6`; index avg `-0.0267` n `26`; metal avg `-0.0585` n `20`; unknown avg `3.2424` n `790`
- 4h: commodity avg `-0.1178` n `12`; crypto_alt avg `1.3617` n `232`; crypto_major avg `1.1115` n `8`; equity avg `0.4381` n `133`; fx avg `-0.0047` n `6`; index avg `0.0558` n `26`; metal avg `-0.1062` n `20`; unknown avg `3.1709` n `790`
- 24h: commodity avg `-0.1395` n `12`; crypto_alt avg `4.8391` n `232`; crypto_major avg `5.6242` n `8`; equity avg `1.432` n `133`; fx avg `-0.2695` n `6`; index avg `0.1766` n `26`; metal avg `0.8176` n `20`; unknown avg `1.5247` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
