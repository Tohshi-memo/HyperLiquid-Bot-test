# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T09:52:23.686726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.0603` n `231`; crypto_major avg `-0.0889` n `8`; equity avg `-0.028` n `128`; fx avg `0.0013` n `6`; index avg `0.0047` n `26`; metal avg `0.0037` n `20`; unknown avg `-0.0191` n `793`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.0459` n `231`; crypto_major avg `-0.1473` n `8`; equity avg `-0.0196` n `128`; fx avg `0.0012` n `6`; index avg `0.0141` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.0068` n `793`
- 4h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.1175` n `231`; crypto_major avg `-0.2893` n `8`; equity avg `-0.045` n `128`; fx avg `0.0026` n `6`; index avg `-0.0019` n `26`; metal avg `0.0013` n `20`; unknown avg `-0.172` n `759`
- 24h: commodity avg `-0.0245` n `12`; crypto_alt avg `0.9564` n `231`; crypto_major avg `0.6291` n `8`; equity avg `0.2345` n `128`; fx avg `0.0106` n `6`; index avg `0.0796` n `26`; metal avg `0.09` n `20`; unknown avg `0.7859` n `716`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
