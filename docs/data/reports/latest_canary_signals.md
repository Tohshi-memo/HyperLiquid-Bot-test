# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T09:22:26.526917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.0158` n `234`; crypto_major avg `0.1112` n `8`; equity avg `-0.0469` n `137`; fx avg `-0.0097` n `6`; index avg `-0.0092` n `27`; metal avg `0.0263` n `20`; unknown avg `0.0298` n `921`
- 1h: commodity avg `-0.0793` n `12`; crypto_alt avg `0.2343` n `234`; crypto_major avg `0.3638` n `8`; equity avg `0.3331` n `137`; fx avg `-0.0267` n `6`; index avg `0.0672` n `27`; metal avg `-0.0592` n `20`; unknown avg `0.5822` n `911`
- 4h: commodity avg `-0.1858` n `12`; crypto_alt avg `0.8256` n `234`; crypto_major avg `0.7284` n `8`; equity avg `0.6634` n `137`; fx avg `0.0289` n `6`; index avg `0.1039` n `27`; metal avg `0.1156` n `20`; unknown avg `0.035` n `891`
- 24h: commodity avg `-0.625` n `12`; crypto_alt avg `3.6288` n `234`; crypto_major avg `2.1465` n `8`; equity avg `1.5583` n `137`; fx avg `0.0618` n `6`; index avg `0.139` n `27`; metal avg `-0.0706` n `20`; unknown avg `0.7014` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
