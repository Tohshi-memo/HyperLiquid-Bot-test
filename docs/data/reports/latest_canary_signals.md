# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T03:07:32.030458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `0.2301` n `234`; crypto_major avg `0.1821` n `8`; equity avg `0.1377` n `140`; fx avg `0.0912` n `6`; index avg `0.0433` n `26`; metal avg `-0.0126` n `20`; unknown avg `0.7671` n `917`
- 1h: commodity avg `0.0216` n `12`; crypto_alt avg `0.5536` n `234`; crypto_major avg `0.4113` n `8`; equity avg `0.3341` n `140`; fx avg `0.0506` n `6`; index avg `0.0632` n `26`; metal avg `0.0399` n `20`; unknown avg `3.8986` n `907`
- 4h: commodity avg `-0.0217` n `12`; crypto_alt avg `2.0757` n `234`; crypto_major avg `1.245` n `8`; equity avg `0.1911` n `140`; fx avg `0.1475` n `6`; index avg `-0.0226` n `26`; metal avg `0.1779` n `20`; unknown avg `1.3838` n `901`
- 24h: commodity avg `-0.2886` n `12`; crypto_alt avg `4.7145` n `234`; crypto_major avg `2.6071` n `8`; equity avg `1.7124` n `140`; fx avg `0.1447` n `6`; index avg `0.2497` n `26`; metal avg `0.5072` n `20`; unknown avg `1.5728` n `757`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
