# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T13:37:32.440366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0617` n `12`; crypto_alt avg `-0.5262` n `234`; crypto_major avg `-0.6844` n `8`; equity avg `-0.1268` n `137`; fx avg `0.0348` n `6`; index avg `-0.0299` n `27`; metal avg `-0.0363` n `20`; unknown avg `499.087` n `919`
- 1h: commodity avg `0.1121` n `12`; crypto_alt avg `-0.5416` n `234`; crypto_major avg `-0.6294` n `8`; equity avg `-0.0212` n `137`; fx avg `0.0265` n `6`; index avg `-0.0298` n `27`; metal avg `0.0091` n `20`; unknown avg `1560.9219` n `917`
- 4h: commodity avg `-0.2478` n `12`; crypto_alt avg `-0.4021` n `234`; crypto_major avg `-0.3754` n `8`; equity avg `0.4809` n `137`; fx avg `-0.0447` n `6`; index avg `0.1603` n `27`; metal avg `0.3655` n `20`; unknown avg `2.5043` n `911`
- 24h: commodity avg `-0.6869` n `12`; crypto_alt avg `3.2303` n `234`; crypto_major avg `2.0231` n `8`; equity avg `1.9049` n `137`; fx avg `0.042` n `6`; index avg `0.2514` n `27`; metal avg `0.2296` n `20`; unknown avg `0.8621` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
