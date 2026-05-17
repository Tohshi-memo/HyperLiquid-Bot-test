# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T16:22:19.193329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `-0.0254` n `228`; crypto_major avg `-0.0154` n `8`; equity avg `0.0315` n `65`; fx avg `0.0` n `5`; index avg `0.0063` n `23`; metal avg `-0.0081` n `18`; unknown avg `0.0563` n `384`
- 1h: commodity avg `0.0676` n `12`; crypto_alt avg `0.1562` n `228`; crypto_major avg `0.0592` n `8`; equity avg `0.0677` n `65`; fx avg `0.0` n `5`; index avg `0.0436` n `23`; metal avg `-0.0017` n `18`; unknown avg `-0.0121` n `384`
- 4h: commodity avg `0.0558` n `12`; crypto_alt avg `-0.205` n `228`; crypto_major avg `-0.2163` n `8`; equity avg `0.1172` n `65`; fx avg `0.0189` n `5`; index avg `0.1433` n `23`; metal avg `0.0188` n `18`; unknown avg `-0.0818` n `383`
- 24h: commodity avg `1.8308` n `12`; crypto_alt avg `-9.1742` n `228`; crypto_major avg `-2.393` n `8`; equity avg `-2.5421` n `65`; fx avg `-0.1657` n `5`; index avg `-1.5746` n `23`; metal avg `-5.836` n `18`; unknown avg `550.046` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
