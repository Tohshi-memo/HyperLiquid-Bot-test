# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T12:07:16.016934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `0.3952` n `228`; crypto_major avg `0.3377` n `8`; equity avg `0.1687` n `66`; fx avg `0.0022` n `5`; index avg `0.0554` n `23`; metal avg `0.0113` n `18`; unknown avg `0.0996` n `383`
- 1h: commodity avg `-0.6324` n `12`; crypto_alt avg `1.1518` n `228`; crypto_major avg `1.0465` n `8`; equity avg `0.5664` n `66`; fx avg `-0.0202` n `5`; index avg `0.1329` n `23`; metal avg `0.5885` n `18`; unknown avg `0.2985` n `383`
- 4h: commodity avg `-0.2383` n `12`; crypto_alt avg `0.5895` n `228`; crypto_major avg `0.5583` n `8`; equity avg `0.305` n `66`; fx avg `0.0339` n `5`; index avg `0.088` n `23`; metal avg `0.391` n `18`; unknown avg `-0.1605` n `383`
- 24h: commodity avg `0.3092` n `12`; crypto_alt avg `-2.1479` n `228`; crypto_major avg `-0.9765` n `8`; equity avg `0.2948` n `65`; fx avg `0.0862` n `5`; index avg `0.135` n `23`; metal avg `0.4569` n `18`; unknown avg `-0.474` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
