# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T18:41:39.666380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `0.0479` n `230`; crypto_major avg `0.0924` n `8`; equity avg `0.0199` n `113`; fx avg `-0.0082` n `6`; index avg `0.0147` n `25`; metal avg `0.0104` n `20`; unknown avg `0.0292` n `786`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0918` n `230`; crypto_major avg `-0.0834` n `8`; equity avg `0.1319` n `113`; fx avg `-0.0093` n `6`; index avg `0.0213` n `25`; metal avg `0.0195` n `20`; unknown avg `1.4318` n `786`
- 4h: commodity avg `0.0132` n `12`; crypto_alt avg `0.0746` n `230`; crypto_major avg `0.2463` n `8`; equity avg `0.6967` n `113`; fx avg `-0.0047` n `6`; index avg `0.0069` n `25`; metal avg `-0.1754` n `20`; unknown avg `0.2273` n `786`
- 24h: commodity avg `0.095` n `12`; crypto_alt avg `0.0276` n `230`; crypto_major avg `1.0193` n `8`; equity avg `4.2003` n `113`; fx avg `0.0314` n `6`; index avg `0.4851` n `25`; metal avg `0.2612` n `20`; unknown avg `0.1961` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2271`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
