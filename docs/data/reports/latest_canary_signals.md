# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T15:34:39.011754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0079` n `230`; crypto_major avg `-0.0213` n `8`; equity avg `-0.0042` n `100`; fx avg `-0.0031` n `6`; index avg `-0.003` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0187` n `775`
- 1h: commodity avg `-0.0394` n `12`; crypto_alt avg `0.218` n `230`; crypto_major avg `0.3696` n `8`; equity avg `0.0788` n `100`; fx avg `-0.0044` n `6`; index avg `0.0167` n `25`; metal avg `-0.0085` n `20`; unknown avg `0.0053` n `775`
- 4h: commodity avg `0.0504` n `12`; crypto_alt avg `-0.0007` n `230`; crypto_major avg `0.2849` n `8`; equity avg `0.1181` n `100`; fx avg `-0.0009` n `6`; index avg `0.0205` n `25`; metal avg `0.005` n `20`; unknown avg `-0.068` n `775`
- 24h: commodity avg `-0.4377` n `12`; crypto_alt avg `1.1275` n `230`; crypto_major avg `1.3572` n `8`; equity avg `0.8798` n `100`; fx avg `0.0135` n `6`; index avg `0.1827` n `25`; metal avg `0.1661` n `20`; unknown avg `0.1471` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
