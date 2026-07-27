# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T04:59:48.376365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0771` n `230`; crypto_major avg `-0.0995` n `8`; equity avg `0.1104` n `100`; fx avg `0.0013` n `6`; index avg `0.0351` n `25`; metal avg `-0.0123` n `20`; unknown avg `-0.1595` n `775`
- 1h: commodity avg `-0.1135` n `12`; crypto_alt avg `-0.0044` n `230`; crypto_major avg `0.0769` n `8`; equity avg `0.2347` n `100`; fx avg `0.0083` n `6`; index avg `0.074` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0267` n `775`
- 4h: commodity avg `-0.0501` n `12`; crypto_alt avg `-0.0218` n `230`; crypto_major avg `0.1129` n `8`; equity avg `0.1289` n `100`; fx avg `0.0248` n `6`; index avg `-0.0487` n `25`; metal avg `-0.1375` n `20`; unknown avg `-0.5022` n `775`
- 24h: commodity avg `-0.5285` n `12`; crypto_alt avg `1.0704` n `230`; crypto_major avg `1.1907` n `8`; equity avg `0.8793` n `100`; fx avg `0.0731` n `6`; index avg `0.1011` n `25`; metal avg `0.308` n `20`; unknown avg `-0.0226` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
