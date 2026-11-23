# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T10:22:32.197159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `-0.006` n `239`; crypto_major avg `-0.067` n `8`; equity avg `0.0634` n `166`; fx avg `-0.0144` n `6`; index avg `0.0227` n `27`; metal avg `0.0055` n `20`; unknown avg `-0.1461` n `1264`
- 1h: commodity avg `0.0639` n `13`; crypto_alt avg `-0.2931` n `239`; crypto_major avg `-0.4887` n `8`; equity avg `-0.2911` n `166`; fx avg `-0.0291` n `6`; index avg `-0.0233` n `27`; metal avg `-0.0611` n `20`; unknown avg `158.7922` n `1260`
- 4h: commodity avg `-0.2824` n `13`; crypto_alt avg `0.3356` n `239`; crypto_major avg `0.1451` n `8`; equity avg `1.0203` n `166`; fx avg `-0.0639` n `6`; index avg `0.0983` n `27`; metal avg `0.0643` n `20`; unknown avg `294.1287` n `1104`
- 24h: commodity avg `-0.7267` n `13`; crypto_alt avg `0.7573` n `239`; crypto_major avg `0.83` n `8`; equity avg `2.3256` n `166`; fx avg `0.1921` n `6`; index avg `0.1242` n `27`; metal avg `0.415` n `20`; unknown avg `0.163` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
