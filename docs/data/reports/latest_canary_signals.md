# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T11:22:27.408671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `-0.081` n `232`; crypto_major avg `-0.0058` n `8`; equity avg `0.0361` n `134`; fx avg `0.0031` n `6`; index avg `0.009` n `26`; metal avg `0.0545` n `20`; unknown avg `1.6199` n `797`
- 1h: commodity avg `0.0979` n `12`; crypto_alt avg `-0.6822` n `232`; crypto_major avg `-0.6106` n `8`; equity avg `-0.1238` n `134`; fx avg `0.0161` n `6`; index avg `-0.0413` n `26`; metal avg `-0.0541` n `20`; unknown avg `0.599` n `795`
- 4h: commodity avg `0.0198` n `12`; crypto_alt avg `0.4013` n `232`; crypto_major avg `0.1902` n `8`; equity avg `0.0841` n `134`; fx avg `-0.0071` n `6`; index avg `0.0032` n `26`; metal avg `-0.0543` n `20`; unknown avg `0.9094` n `787`
- 24h: commodity avg `0.2303` n `12`; crypto_alt avg `0.1994` n `232`; crypto_major avg `-0.9452` n `8`; equity avg `-0.0335` n `134`; fx avg `-0.1248` n `6`; index avg `-0.0259` n `26`; metal avg `0.1633` n `20`; unknown avg `7463.4342` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
