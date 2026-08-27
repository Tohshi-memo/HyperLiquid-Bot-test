# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T05:37:24.965319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.1192` n `231`; crypto_major avg `-0.0151` n `8`; equity avg `-0.0322` n `127`; fx avg `-0.0006` n `6`; index avg `-0.0134` n `26`; metal avg `-0.0633` n `20`; unknown avg `-0.2149` n `791`
- 1h: commodity avg `-0.0482` n `12`; crypto_alt avg `-0.3548` n `231`; crypto_major avg `0.0882` n `8`; equity avg `-0.1713` n `127`; fx avg `0.0012` n `6`; index avg `-0.057` n `26`; metal avg `-0.0339` n `20`; unknown avg `-0.3148` n `791`
- 4h: commodity avg `-0.0499` n `12`; crypto_alt avg `-0.9934` n `231`; crypto_major avg `-0.6146` n `8`; equity avg `-0.1657` n `127`; fx avg `0.0239` n `6`; index avg `-0.0726` n `26`; metal avg `-0.111` n `20`; unknown avg `-0.4019` n `791`
- 24h: commodity avg `0.3322` n `12`; crypto_alt avg `-0.3969` n `231`; crypto_major avg `-0.0175` n `8`; equity avg `0.9984` n `127`; fx avg `-0.0994` n `6`; index avg `0.1734` n `26`; metal avg `-0.3056` n `20`; unknown avg `0.2503` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
