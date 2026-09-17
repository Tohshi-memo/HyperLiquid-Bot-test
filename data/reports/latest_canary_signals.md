# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T13:07:28.868716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `0.0981` n `234`; crypto_major avg `0.097` n `8`; equity avg `0.0781` n `137`; fx avg `0.0059` n `6`; index avg `0.0032` n `27`; metal avg `-0.0036` n `20`; unknown avg `-0.3307` n `919`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.2563` n `234`; crypto_major avg `0.6211` n `8`; equity avg `0.5105` n `137`; fx avg `-0.0253` n `6`; index avg `0.1022` n `27`; metal avg `0.133` n `20`; unknown avg `14.1867` n `913`
- 4h: commodity avg `-0.2906` n `12`; crypto_alt avg `-0.0287` n `234`; crypto_major avg `0.1761` n `8`; equity avg `0.5726` n `137`; fx avg `-0.0727` n `6`; index avg `0.1882` n `27`; metal avg `0.3529` n `20`; unknown avg `0.0478` n `913`
- 24h: commodity avg `-0.8426` n `12`; crypto_alt avg `3.6259` n `234`; crypto_major avg `2.332` n `8`; equity avg `2.0914` n `137`; fx avg `0.0227` n `6`; index avg `0.2906` n `27`; metal avg `0.195` n `20`; unknown avg `0.5201` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
