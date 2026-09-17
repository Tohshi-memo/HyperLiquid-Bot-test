# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T00:07:27.244583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `0.0396` n `234`; crypto_major avg `-0.099` n `8`; equity avg `0.0312` n `137`; fx avg `-0.0331` n `6`; index avg `0.001` n `27`; metal avg `-0.0037` n `20`; unknown avg `0.5082` n `917`
- 1h: commodity avg `-0.0724` n `12`; crypto_alt avg `1.394` n `234`; crypto_major avg `0.8111` n `8`; equity avg `0.4504` n `137`; fx avg `-0.0381` n `6`; index avg `0.1227` n `27`; metal avg `0.1169` n `20`; unknown avg `0.642` n `915`
- 4h: commodity avg `-0.0476` n `12`; crypto_alt avg `1.3355` n `234`; crypto_major avg `-0.0644` n `8`; equity avg `0.9298` n `137`; fx avg `-0.0546` n `6`; index avg `0.1967` n `27`; metal avg `0.0966` n `20`; unknown avg `0.923` n `793`
- 24h: commodity avg `-0.6303` n `12`; crypto_alt avg `1.2628` n `234`; crypto_major avg `1.0713` n `8`; equity avg `1.714` n `137`; fx avg `0.0031` n `6`; index avg `0.2087` n `27`; metal avg `-0.1625` n `20`; unknown avg `-0.2381` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
