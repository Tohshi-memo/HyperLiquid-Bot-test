# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T13:52:29.030292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0633` n `12`; crypto_alt avg `0.2851` n `234`; crypto_major avg `0.4158` n `8`; equity avg `0.2526` n `137`; fx avg `-0.0147` n `6`; index avg `0.0291` n `27`; metal avg `0.0393` n `20`; unknown avg `0.463` n `899`
- 1h: commodity avg `0.1581` n `12`; crypto_alt avg `-0.0293` n `234`; crypto_major avg `0.0213` n `8`; equity avg `0.2173` n `137`; fx avg `0.0235` n `6`; index avg `-0.0001` n `27`; metal avg `0.0632` n `20`; unknown avg `-0.0315` n `897`
- 4h: commodity avg `-0.1223` n `12`; crypto_alt avg `0.1281` n `234`; crypto_major avg `0.4426` n `8`; equity avg `0.8181` n `137`; fx avg `-0.0609` n `6`; index avg `0.1964` n `27`; metal avg `0.4212` n `20`; unknown avg `0.6846` n `891`
- 24h: commodity avg `-0.5312` n `12`; crypto_alt avg `3.2412` n `234`; crypto_major avg `2.1339` n `8`; equity avg `1.7212` n `137`; fx avg `0.0281` n `6`; index avg `0.2388` n `27`; metal avg `0.3023` n `20`; unknown avg `28.3131` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
