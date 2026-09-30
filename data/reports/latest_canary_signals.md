# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T00:37:26.796768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.3319` n `234`; crypto_major avg `0.1921` n `8`; equity avg `0.0177` n `142`; fx avg `0.0456` n `6`; index avg `-0.0044` n `26`; metal avg `0.0005` n `20`; unknown avg `1.2979` n `963`
- 1h: commodity avg `0.0178` n `12`; crypto_alt avg `-0.0495` n `234`; crypto_major avg `-0.153` n `8`; equity avg `-0.0143` n `142`; fx avg `0.0586` n `6`; index avg `-0.001` n `26`; metal avg `-0.0179` n `20`; unknown avg `0.9815` n `955`
- 4h: commodity avg `0.1191` n `12`; crypto_alt avg `-0.7095` n `234`; crypto_major avg `-0.2304` n `8`; equity avg `0.1408` n `142`; fx avg `0.0527` n `6`; index avg `0.0255` n `26`; metal avg `0.0178` n `20`; unknown avg `1.7077` n `924`
- 24h: commodity avg `-0.8576` n `12`; crypto_alt avg `-0.4187` n `234`; crypto_major avg `-0.5968` n `8`; equity avg `0.7407` n `142`; fx avg `-0.1029` n `6`; index avg `0.1101` n `26`; metal avg `0.2352` n `20`; unknown avg `3099.7913` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1804`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
