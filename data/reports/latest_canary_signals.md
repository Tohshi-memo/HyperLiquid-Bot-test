# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T08:07:28.431257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `12`; crypto_alt avg `0.0014` n `234`; crypto_major avg `0.1232` n `8`; equity avg `0.1206` n `137`; fx avg `0.0163` n `6`; index avg `-0.0184` n `27`; metal avg `-0.0365` n `20`; unknown avg `0.2104` n `919`
- 1h: commodity avg `0.1164` n `12`; crypto_alt avg `0.0289` n `234`; crypto_major avg `0.0697` n `8`; equity avg `0.2129` n `137`; fx avg `0.0324` n `6`; index avg `-0.014` n `27`; metal avg `0.1066` n `20`; unknown avg `0.2944` n `919`
- 4h: commodity avg `-0.1087` n `12`; crypto_alt avg `0.8335` n `234`; crypto_major avg `0.3154` n `8`; equity avg `0.3442` n `137`; fx avg `0.0469` n `6`; index avg `0.0102` n `27`; metal avg `0.1903` n `20`; unknown avg `-0.0261` n `891`
- 24h: commodity avg `-0.4754` n `12`; crypto_alt avg `3.5939` n `234`; crypto_major avg `2.1929` n `8`; equity avg `1.4844` n `137`; fx avg `0.0888` n `6`; index avg `0.1125` n `27`; metal avg `0.0487` n `20`; unknown avg `0.6545` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
