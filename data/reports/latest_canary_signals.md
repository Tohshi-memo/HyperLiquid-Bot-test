# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T13:22:29.564123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0337` n `12`; crypto_alt avg `-0.0718` n `230`; crypto_major avg `-0.165` n `8`; equity avg `0.0662` n `98`; fx avg `-0.0193` n `6`; index avg `-0.0016` n `25`; metal avg `-0.1099` n `20`; unknown avg `-0.0038` n `771`
- 1h: commodity avg `0.0134` n `12`; crypto_alt avg `-0.1047` n `230`; crypto_major avg `-0.0086` n `8`; equity avg `0.1194` n `98`; fx avg `-0.0303` n `6`; index avg `0.0017` n `25`; metal avg `-0.1342` n `20`; unknown avg `0.0388` n `771`
- 4h: commodity avg `0.2974` n `12`; crypto_alt avg `0.0718` n `230`; crypto_major avg `0.088` n `8`; equity avg `-0.1305` n `98`; fx avg `-0.0268` n `6`; index avg `-0.0178` n `25`; metal avg `-0.1898` n `20`; unknown avg `0.0569` n `771`
- 24h: commodity avg `0.4453` n `12`; crypto_alt avg `1.824` n `230`; crypto_major avg `2.1958` n `8`; equity avg `1.2442` n `98`; fx avg `-0.0834` n `6`; index avg `0.1731` n `25`; metal avg `0.501` n `20`; unknown avg `0.1315` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0888`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.061`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0608`, n `666`, weak_sample_signal
