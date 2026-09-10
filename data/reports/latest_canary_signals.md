# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T05:22:27.679973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.2981` n `233`; crypto_major avg `0.0913` n `8`; equity avg `0.0525` n `134`; fx avg `0.0042` n `6`; index avg `0.0117` n `26`; metal avg `0.0302` n `20`; unknown avg `-0.0861` n `797`
- 1h: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0034` n `233`; crypto_major avg `-0.1388` n `8`; equity avg `0.1162` n `134`; fx avg `-0.0013` n `6`; index avg `0.0398` n `26`; metal avg `0.0272` n `20`; unknown avg `0.5931` n `789`
- 4h: commodity avg `-0.1105` n `12`; crypto_alt avg `0.3337` n `233`; crypto_major avg `0.3782` n `8`; equity avg `0.3605` n `134`; fx avg `-0.0213` n `6`; index avg `0.1394` n `26`; metal avg `0.043` n `20`; unknown avg `1.3307` n `789`
- 24h: commodity avg `0.0447` n `12`; crypto_alt avg `-3.5876` n `233`; crypto_major avg `-2.4688` n `8`; equity avg `-0.888` n `134`; fx avg `0.0348` n `6`; index avg `-0.1005` n `26`; metal avg `0.4253` n `20`; unknown avg `1.2309` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
