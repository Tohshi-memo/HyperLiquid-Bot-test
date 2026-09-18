# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T08:37:26.667155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `0.0436` n `234`; crypto_major avg `-0.1161` n `8`; equity avg `-0.0335` n `140`; fx avg `-0.0018` n `6`; index avg `-0.016` n `26`; metal avg `-0.0344` n `20`; unknown avg `-0.0378` n `921`
- 1h: commodity avg `0.1595` n `12`; crypto_alt avg `0.1786` n `234`; crypto_major avg `0.1193` n `8`; equity avg `-0.019` n `140`; fx avg `0.063` n `6`; index avg `-0.0192` n `26`; metal avg `-0.0603` n `20`; unknown avg `0.1459` n `919`
- 4h: commodity avg `-0.0933` n `12`; crypto_alt avg `0.9153` n `234`; crypto_major avg `0.8118` n `8`; equity avg `0.5909` n `140`; fx avg `0.0382` n `6`; index avg `0.0895` n `26`; metal avg `0.3063` n `20`; unknown avg `-0.1689` n `863`
- 24h: commodity avg `-0.2454` n `12`; crypto_alt avg `5.1067` n `234`; crypto_major avg `3.7295` n `8`; equity avg `2.0611` n `140`; fx avg `0.1714` n `6`; index avg `0.3269` n `26`; metal avg `0.6459` n `20`; unknown avg `2.2321` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
