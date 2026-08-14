# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T21:52:30.172183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0234` n `12`; crypto_alt avg `-0.0478` n `230`; crypto_major avg `-0.0406` n `8`; equity avg `0.0137` n `114`; fx avg `0.0037` n `6`; index avg `-0.0013` n `25`; metal avg `0.0081` n `20`; unknown avg `0.126` n `791`
- 1h: commodity avg `0.0075` n `12`; crypto_alt avg `0.0022` n `230`; crypto_major avg `0.0244` n `8`; equity avg `0.017` n `114`; fx avg `-0.0158` n `6`; index avg `0.0116` n `25`; metal avg `0.0341` n `20`; unknown avg `0.1768` n `791`
- 4h: commodity avg `-0.0573` n `12`; crypto_alt avg `-0.186` n `230`; crypto_major avg `-0.178` n `8`; equity avg `0.1814` n `114`; fx avg `0.0187` n `6`; index avg `0.0523` n `25`; metal avg `0.0351` n `20`; unknown avg `8.5558` n `791`
- 24h: commodity avg `0.1852` n `12`; crypto_alt avg `0.0654` n `230`; crypto_major avg `-0.978` n `8`; equity avg `-0.5089` n `114`; fx avg `0.0728` n `6`; index avg `-0.0667` n `25`; metal avg `0.2377` n `20`; unknown avg `-0.0986` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
