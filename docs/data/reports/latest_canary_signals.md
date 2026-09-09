# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T08:52:31.842450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0168` n `12`; crypto_alt avg `0.0188` n `233`; crypto_major avg `0.0413` n `8`; equity avg `-0.0325` n `134`; fx avg `0.0015` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.2081` n `798`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `0.3152` n `233`; crypto_major avg `0.169` n `8`; equity avg `0.1592` n `134`; fx avg `0.0472` n `6`; index avg `-0.0052` n `26`; metal avg `-0.1003` n `20`; unknown avg `0.0716` n `790`
- 4h: commodity avg `0.1206` n `12`; crypto_alt avg `0.732` n `233`; crypto_major avg `0.3481` n `8`; equity avg `0.1668` n `134`; fx avg `0.0113` n `6`; index avg `-0.0274` n `26`; metal avg `0.1812` n `20`; unknown avg `0.6801` n `772`
- 24h: commodity avg `-0.2386` n `12`; crypto_alt avg `0.9521` n `232`; crypto_major avg `1.7212` n `8`; equity avg `1.7095` n `134`; fx avg `-0.0875` n `6`; index avg `0.1093` n `26`; metal avg `0.0725` n `20`; unknown avg `0.5031` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
