# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T20:57:15.800354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.043` n `13`; crypto_alt avg `0.2041` n `239`; crypto_major avg `0.3056` n `8`; equity avg `-0.236` n `161`; fx avg `-0.0062` n `6`; index avg `-0.0242` n `27`; metal avg `-0.0169` n `20`; unknown avg `6.3786` n `1258`
- 1h: commodity avg `0.0714` n `13`; crypto_alt avg `0.3026` n `239`; crypto_major avg `0.3598` n `8`; equity avg `-0.3799` n `161`; fx avg `0.0007` n `6`; index avg `-0.0371` n `27`; metal avg `-0.0451` n `20`; unknown avg `6.9042` n `1246`
- 4h: commodity avg `-0.3659` n `13`; crypto_alt avg `-0.4738` n `239`; crypto_major avg `0.111` n `8`; equity avg `-0.9428` n `161`; fx avg `0.0017` n `6`; index avg `-0.0448` n `27`; metal avg `-0.1647` n `20`; unknown avg `5.8927` n `1246`
- 24h: commodity avg `0.1642` n `13`; crypto_alt avg `0.7744` n `239`; crypto_major avg `1.1865` n `8`; equity avg `4.4742` n `161`; fx avg `-0.1468` n `6`; index avg `0.4624` n `27`; metal avg `-0.0788` n `20`; unknown avg `7.8411` n `1155`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.142`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.124`, n `670`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1235`, n `670`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1197`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1172`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `670`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1064`, n `670`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1014`, n `670`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0947`, n `670`, weak_sample_signal
