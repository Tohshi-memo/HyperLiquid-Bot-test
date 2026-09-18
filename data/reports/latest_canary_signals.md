# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T11:22:28.022260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `-0.0602` n `234`; crypto_major avg `0.0669` n `8`; equity avg `-0.0775` n `140`; fx avg `-0.0008` n `6`; index avg `-0.0301` n `26`; metal avg `0.0094` n `20`; unknown avg `0.2105` n `927`
- 1h: commodity avg `0.0146` n `12`; crypto_alt avg `-0.9408` n `234`; crypto_major avg `-0.3708` n `8`; equity avg `-0.2447` n `140`; fx avg `-0.018` n `6`; index avg `-0.042` n `26`; metal avg `0.0578` n `20`; unknown avg `2.0602` n `923`
- 4h: commodity avg `0.1741` n `12`; crypto_alt avg `-0.0264` n `234`; crypto_major avg `0.2954` n `8`; equity avg `-0.3753` n `140`; fx avg `0.0945` n `6`; index avg `-0.0994` n `26`; metal avg `0.0093` n `20`; unknown avg `0.9128` n `917`
- 24h: commodity avg `-0.0619` n `12`; crypto_alt avg `5.0042` n `234`; crypto_major avg `4.3541` n `8`; equity avg `1.4827` n `140`; fx avg `0.2283` n `6`; index avg `0.1517` n `26`; metal avg `0.5746` n `20`; unknown avg `1.9304` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
