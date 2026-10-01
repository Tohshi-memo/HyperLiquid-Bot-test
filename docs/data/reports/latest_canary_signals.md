# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T00:37:41.992729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `0.0506` n `234`; crypto_major avg `-0.0761` n `8`; equity avg `-0.1439` n `142`; fx avg `0.0601` n `6`; index avg `-0.0272` n `26`; metal avg `-0.0394` n `20`; unknown avg `2.4124` n `959`
- 1h: commodity avg `0.078` n `12`; crypto_alt avg `-0.1396` n `234`; crypto_major avg `-0.2545` n `8`; equity avg `-0.2267` n `142`; fx avg `0.0957` n `6`; index avg `-0.0612` n `26`; metal avg `-0.1447` n `20`; unknown avg `1.2729` n `943`
- 4h: commodity avg `0.0241` n `12`; crypto_alt avg `0.231` n `234`; crypto_major avg `-0.0918` n `8`; equity avg `-0.211` n `142`; fx avg `0.1095` n `6`; index avg `-0.0154` n `26`; metal avg `-0.161` n `20`; unknown avg `0.6386` n `941`
- 24h: commodity avg `0.2454` n `12`; crypto_alt avg `1.0346` n `234`; crypto_major avg `0.834` n `8`; equity avg `-0.5413` n `142`; fx avg `0.1373` n `6`; index avg `-0.0649` n `26`; metal avg `-0.3933` n `20`; unknown avg `777.4731` n `797`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
