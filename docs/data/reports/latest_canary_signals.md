# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T18:52:12.916414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `0.0718` n `228`; crypto_major avg `0.1032` n `8`; equity avg `0.0579` n `65`; fx avg `0.0017` n `5`; index avg `0.0054` n `23`; metal avg `-0.0028` n `18`; unknown avg `0.0075` n `384`
- 1h: commodity avg `0.0751` n `12`; crypto_alt avg `0.1219` n `228`; crypto_major avg `0.3344` n `8`; equity avg `0.0675` n `65`; fx avg `0.0005` n `5`; index avg `0.0076` n `23`; metal avg `-0.0569` n `18`; unknown avg `-0.0317` n `384`
- 4h: commodity avg `0.1636` n `12`; crypto_alt avg `-0.3231` n `228`; crypto_major avg `0.3566` n `8`; equity avg `0.0748` n `65`; fx avg `0.0112` n `5`; index avg `0.0492` n `23`; metal avg `-0.0212` n `18`; unknown avg `-0.0296` n `384`
- 24h: commodity avg `1.8633` n `12`; crypto_alt avg `-9.563` n `228`; crypto_major avg `-2.1788` n `8`; equity avg `-2.5495` n `65`; fx avg `-0.1538` n `5`; index avg `-1.5943` n `23`; metal avg `-5.8942` n `18`; unknown avg `550.0459` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
