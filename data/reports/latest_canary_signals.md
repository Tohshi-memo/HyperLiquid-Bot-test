# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T12:52:29.443886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `-0.2295` n `234`; crypto_major avg `-0.2381` n `8`; equity avg `0.0154` n `137`; fx avg `-0.0117` n `6`; index avg `-0.0006` n `27`; metal avg `-0.0146` n `20`; unknown avg `385.923` n `921`
- 1h: commodity avg `-0.1439` n `12`; crypto_alt avg `0.3412` n `234`; crypto_major avg `0.8303` n `8`; equity avg `0.5985` n `137`; fx avg `-0.0454` n `6`; index avg `0.1637` n `27`; metal avg `0.2262` n `20`; unknown avg `5.7411` n `913`
- 4h: commodity avg `-0.2483` n `12`; crypto_alt avg `-0.0732` n `234`; crypto_major avg `0.2576` n `8`; equity avg `0.6187` n `137`; fx avg `-0.0693` n `6`; index avg `0.2266` n `27`; metal avg `0.3957` n `20`; unknown avg `0.2674` n `913`
- 24h: commodity avg `-0.8247` n `12`; crypto_alt avg `3.2812` n `234`; crypto_major avg `1.8374` n `8`; equity avg `1.842` n `137`; fx avg `0.0256` n `6`; index avg `0.2665` n `27`; metal avg `0.1831` n `20`; unknown avg `0.2663` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
