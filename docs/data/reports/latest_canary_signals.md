# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T15:37:27.794874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `0.4461` n `234`; crypto_major avg `0.4513` n `8`; equity avg `0.1228` n `138`; fx avg `-0.0212` n `6`; index avg `0.0216` n `26`; metal avg `0.0139` n `20`; unknown avg `0.5746` n `917`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `-0.3269` n `234`; crypto_major avg `-0.4286` n `8`; equity avg `-0.0717` n `138`; fx avg `-0.0243` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0742` n `20`; unknown avg `0.6752` n `915`
- 4h: commodity avg `0.0919` n `12`; crypto_alt avg `0.7931` n `234`; crypto_major avg `1.1819` n `8`; equity avg `0.541` n `138`; fx avg `-0.0696` n `6`; index avg `0.1479` n `26`; metal avg `0.2653` n `20`; unknown avg `1.5065` n `891`
- 24h: commodity avg `-0.1937` n `12`; crypto_alt avg `4.6105` n `234`; crypto_major avg `2.672` n `8`; equity avg `1.4084` n `138`; fx avg `0.0231` n `6`; index avg `0.2165` n `26`; metal avg `0.1532` n `20`; unknown avg `0.3973` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
