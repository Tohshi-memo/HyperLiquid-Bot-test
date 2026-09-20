# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T21:52:31.053086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `0.1169` n `234`; crypto_major avg `-0.0368` n `8`; equity avg `0.0117` n `140`; fx avg `-0.0055` n `6`; index avg `0.0` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.2963` n `943`
- 1h: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.0405` n `234`; crypto_major avg `-0.3209` n `8`; equity avg `-0.0185` n `140`; fx avg `-0.0476` n `6`; index avg `0.0` n `26`; metal avg `-0.0174` n `20`; unknown avg `20.2386` n `921`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.3363` n `234`; crypto_major avg `-0.1984` n `8`; equity avg `0.0378` n `140`; fx avg `-0.0442` n `6`; index avg `0.0105` n `26`; metal avg `-0.0447` n `20`; unknown avg `0.6169` n `873`
- 24h: commodity avg `0.3508` n `12`; crypto_alt avg `1.402` n `234`; crypto_major avg `-0.0159` n `8`; equity avg `-0.0937` n `140`; fx avg `-0.043` n `6`; index avg `-0.0481` n `26`; metal avg `-0.0524` n `20`; unknown avg `2.7716` n `777`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
