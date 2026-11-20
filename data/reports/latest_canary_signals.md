# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T03:37:30.654599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `13`; crypto_alt avg `-0.3077` n `239`; crypto_major avg `-0.1824` n `8`; equity avg `-0.1717` n `165`; fx avg `-0.0056` n `6`; index avg `-0.0203` n `27`; metal avg `0.012` n `20`; unknown avg `158.2914` n `1262`
- 1h: commodity avg `-0.0229` n `13`; crypto_alt avg `0.2641` n `239`; crypto_major avg `0.5495` n `8`; equity avg `0.0649` n `165`; fx avg `0.0098` n `6`; index avg `-0.0014` n `27`; metal avg `-0.1334` n `20`; unknown avg `215.6699` n `1260`
- 4h: commodity avg `-0.0992` n `13`; crypto_alt avg `-1.3588` n `239`; crypto_major avg `-0.4505` n `8`; equity avg `-0.732` n `165`; fx avg `0.03` n `6`; index avg `-0.0725` n `27`; metal avg `-0.5948` n `20`; unknown avg `0.7854` n `1250`
- 24h: commodity avg `-0.0012` n `13`; crypto_alt avg `-2.6468` n `239`; crypto_major avg `-1.3029` n `8`; equity avg `-5.3785` n `165`; fx avg `0.0568` n `6`; index avg `-0.3993` n `27`; metal avg `-1.5032` n `20`; unknown avg `15.1624` n `1169`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
