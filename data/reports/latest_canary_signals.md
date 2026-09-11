# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T06:52:25.801872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.0181` n `233`; crypto_major avg `0.1225` n `8`; equity avg `0.1126` n `136`; fx avg `0.0112` n `6`; index avg `0.0146` n `26`; metal avg `0.0173` n `20`; unknown avg `-0.1084` n `796`
- 1h: commodity avg `0.0455` n `12`; crypto_alt avg `-0.1187` n `233`; crypto_major avg `0.0571` n `8`; equity avg `0.2344` n `136`; fx avg `0.0439` n `6`; index avg `0.047` n `26`; metal avg `0.0639` n `20`; unknown avg `0.254` n `772`
- 4h: commodity avg `-0.2769` n `12`; crypto_alt avg `0.6879` n `233`; crypto_major avg `0.6603` n `8`; equity avg `0.7148` n `136`; fx avg `0.0145` n `6`; index avg `0.1739` n `26`; metal avg `0.3002` n `20`; unknown avg `27.016` n `764`
- 24h: commodity avg `0.8722` n `12`; crypto_alt avg `-1.8735` n `233`; crypto_major avg `-1.8163` n `8`; equity avg `-1.4719` n `136`; fx avg `0.0569` n `6`; index avg `-0.2535` n `26`; metal avg `-1.0535` n `20`; unknown avg `1.071` n `685`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
