# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T20:07:32.640426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.028` n `12`; crypto_alt avg `0.0658` n `230`; crypto_major avg `0.0449` n `8`; equity avg `0.0225` n `114`; fx avg `-0.0023` n `6`; index avg `0.0118` n `25`; metal avg `-0.0293` n `20`; unknown avg `0.6879` n `791`
- 1h: commodity avg `0.0116` n `12`; crypto_alt avg `0.2186` n `230`; crypto_major avg `0.2435` n `8`; equity avg `0.2968` n `114`; fx avg `0.0102` n `6`; index avg `0.0282` n `25`; metal avg `0.016` n `20`; unknown avg `0.006` n `791`
- 4h: commodity avg `0.0381` n `12`; crypto_alt avg `0.1145` n `230`; crypto_major avg `-0.1466` n `8`; equity avg `0.1588` n `114`; fx avg `-0.0116` n `6`; index avg `0.0362` n `25`; metal avg `-0.0638` n `20`; unknown avg `18.4698` n `791`
- 24h: commodity avg `0.2064` n `12`; crypto_alt avg `0.3106` n `230`; crypto_major avg `-0.9667` n `8`; equity avg `-0.311` n `114`; fx avg `0.0774` n `6`; index avg `-0.0616` n `25`; metal avg `0.2485` n `20`; unknown avg `-0.0027` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
