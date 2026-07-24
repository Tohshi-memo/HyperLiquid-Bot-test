# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T05:52:25.698519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0389` n `12`; crypto_alt avg `0.0467` n `230`; crypto_major avg `0.0053` n `8`; equity avg `-0.0942` n `100`; fx avg `0.0067` n `6`; index avg `0.0056` n `25`; metal avg `-0.031` n `20`; unknown avg `-0.0194` n `772`
- 1h: commodity avg `-0.0451` n `12`; crypto_alt avg `0.0709` n `230`; crypto_major avg `0.1044` n `8`; equity avg `0.2082` n `100`; fx avg `-0.0026` n `6`; index avg `0.0653` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.5381` n `772`
- 4h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.1562` n `230`; crypto_major avg `0.1223` n `8`; equity avg `-0.3863` n `100`; fx avg `0.0118` n `6`; index avg `-0.0927` n `25`; metal avg `-0.1785` n `20`; unknown avg `-0.408` n `772`
- 24h: commodity avg `0.4197` n `12`; crypto_alt avg `-1.0135` n `230`; crypto_major avg `-1.5935` n `8`; equity avg `-1.9891` n `99`; fx avg `-0.0971` n `6`; index avg `-0.5406` n `25`; metal avg `-1.0297` n `20`; unknown avg `-0.0296` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1028`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
