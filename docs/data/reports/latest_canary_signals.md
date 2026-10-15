# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T20:07:33.546776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `-0.182` n `236`; crypto_major avg `-0.0697` n `8`; equity avg `0.1226` n `151`; fx avg `-0.0024` n `6`; index avg `0.0071` n `26`; metal avg `-0.0151` n `20`; unknown avg `0.0837` n `1120`
- 1h: commodity avg `-0.0699` n `13`; crypto_alt avg `-0.2064` n `236`; crypto_major avg `-0.0235` n `8`; equity avg `0.7744` n `151`; fx avg `-0.0017` n `6`; index avg `0.0779` n `26`; metal avg `0.0965` n `20`; unknown avg `1.1698` n `1088`
- 4h: commodity avg `-0.1234` n `13`; crypto_alt avg `0.209` n `236`; crypto_major avg `0.125` n `8`; equity avg `1.4819` n `151`; fx avg `0.0122` n `6`; index avg `0.1578` n `26`; metal avg `0.1474` n `20`; unknown avg `1.4441` n `1088`
- 24h: commodity avg `-0.1902` n `13`; crypto_alt avg `0.7857` n `236`; crypto_major avg `0.5664` n `8`; equity avg `0.1969` n `151`; fx avg `0.1682` n `6`; index avg `-0.0448` n `26`; metal avg `0.5473` n `20`; unknown avg `11.5233` n `928`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0963`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0845`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0775`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.07`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0508`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
