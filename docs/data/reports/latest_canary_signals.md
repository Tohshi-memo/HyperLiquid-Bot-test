# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T23:07:44.839070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `13`; crypto_alt avg `-0.3667` n `239`; crypto_major avg `-0.2351` n `8`; equity avg `-0.2145` n `158`; fx avg `0.0261` n `6`; index avg `-0.0379` n `27`; metal avg `0.0166` n `20`; unknown avg `0.2202` n `1202`
- 1h: commodity avg `0.0363` n `13`; crypto_alt avg `0.2579` n `239`; crypto_major avg `0.3874` n `8`; equity avg `-0.3262` n `158`; fx avg `0.0336` n `6`; index avg `0.0224` n `27`; metal avg `0.0217` n `20`; unknown avg `-0.0116` n `1202`
- 4h: commodity avg `0.0573` n `13`; crypto_alt avg `0.4262` n `239`; crypto_major avg `0.2364` n `8`; equity avg `-0.0751` n `158`; fx avg `0.0404` n `6`; index avg `0.0045` n `27`; metal avg `0.014` n `20`; unknown avg `175.6376` n `1138`
- 24h: commodity avg `-1.8168` n `13`; crypto_alt avg `1.9466` n `239`; crypto_major avg `2.2689` n `8`; equity avg `-1.7274` n `158`; fx avg `0.1029` n `6`; index avg `0.0583` n `27`; metal avg `1.2173` n `20`; unknown avg `29.7582` n `1038`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.266`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
