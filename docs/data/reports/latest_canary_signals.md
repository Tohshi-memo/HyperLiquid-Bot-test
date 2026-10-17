# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T02:07:29.757267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `13`; crypto_alt avg `0.261` n `236`; crypto_major avg `0.1042` n `8`; equity avg `0.0709` n `151`; fx avg `-0.0235` n `6`; index avg `0.0032` n `26`; metal avg `-0.0102` n `20`; unknown avg `-0.0043` n `1191`
- 1h: commodity avg `0.0256` n `13`; crypto_alt avg `0.0044` n `236`; crypto_major avg `0.0727` n `8`; equity avg `-0.0193` n `151`; fx avg `-0.0101` n `6`; index avg `-0.0099` n `26`; metal avg `-0.014` n `20`; unknown avg `-0.1121` n `1189`
- 4h: commodity avg `0.1107` n `13`; crypto_alt avg `0.0326` n `236`; crypto_major avg `-0.1692` n `8`; equity avg `0.2305` n `151`; fx avg `-0.0058` n `6`; index avg `0.0056` n `26`; metal avg `-0.031` n `20`; unknown avg `0.6986` n `1181`
- 24h: commodity avg `0.5707` n `13`; crypto_alt avg `-0.9857` n `236`; crypto_major avg `-0.9464` n `8`; equity avg `-3.6251` n `151`; fx avg `-0.0336` n `6`; index avg `-0.5871` n `26`; metal avg `-0.0541` n `20`; unknown avg `40.1942` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1703`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.094`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0767`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
