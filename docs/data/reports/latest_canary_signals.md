# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T23:52:32.683718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.021` n `12`; crypto_alt avg `-0.1103` n `234`; crypto_major avg `-0.0872` n `8`; equity avg `0.0116` n `142`; fx avg `-0.0037` n `6`; index avg `-0.0053` n `26`; metal avg `0.0112` n `20`; unknown avg `0.9948` n `975`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `-0.0675` n `234`; crypto_major avg `-0.1694` n `8`; equity avg `0.0487` n `142`; fx avg `0.0107` n `6`; index avg `0.0216` n `26`; metal avg `0.0008` n `20`; unknown avg `2.2739` n `973`
- 4h: commodity avg `-0.1291` n `12`; crypto_alt avg `0.8074` n `234`; crypto_major avg `0.6319` n `8`; equity avg `0.1148` n `142`; fx avg `0.0294` n `6`; index avg `0.0501` n `26`; metal avg `0.011` n `20`; unknown avg `1.8836` n `887`
- 24h: commodity avg `0.1565` n `12`; crypto_alt avg `1.0209` n `234`; crypto_major avg `0.8593` n `8`; equity avg `-0.3225` n `142`; fx avg `0.1031` n `6`; index avg `-0.0231` n `26`; metal avg `-0.2842` n `20`; unknown avg `762.0148` n `813`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
