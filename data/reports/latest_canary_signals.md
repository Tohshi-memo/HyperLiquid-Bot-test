# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T14:37:48.155442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `13`; crypto_alt avg `0.0137` n `239`; crypto_major avg `0.2187` n `8`; equity avg `-0.3729` n `162`; fx avg `-0.0093` n `6`; index avg `-0.049` n `27`; metal avg `0.0771` n `20`; unknown avg `2.1444` n `1266`
- 1h: commodity avg `0.0257` n `13`; crypto_alt avg `0.0301` n `239`; crypto_major avg `0.3363` n `8`; equity avg `-0.2927` n `162`; fx avg `0.0281` n `6`; index avg `-0.0429` n `27`; metal avg `0.1727` n `20`; unknown avg `10.1947` n `1262`
- 4h: commodity avg `0.2554` n `13`; crypto_alt avg `1.2251` n `239`; crypto_major avg `1.5912` n `8`; equity avg `1.0125` n `162`; fx avg `0.0334` n `6`; index avg `0.0193` n `27`; metal avg `0.1035` n `20`; unknown avg `4.4745` n `1218`
- 24h: commodity avg `-0.1931` n `13`; crypto_alt avg `0.1782` n `239`; crypto_major avg `0.376` n `8`; equity avg `-1.3145` n `162`; fx avg `-0.0465` n `6`; index avg `-0.2081` n `27`; metal avg `-0.1218` n `20`; unknown avg `10.0154` n `1105`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
