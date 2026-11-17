# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T10:22:27.586777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `13`; crypto_alt avg `-0.0376` n `239`; crypto_major avg `-0.1363` n `8`; equity avg `-0.0321` n `162`; fx avg `-0.0101` n `6`; index avg `0.0066` n `27`; metal avg `-0.0086` n `20`; unknown avg `0.2755` n `1264`
- 1h: commodity avg `0.0658` n `13`; crypto_alt avg `0.1451` n `239`; crypto_major avg `0.0755` n `8`; equity avg `0.2987` n `162`; fx avg `-0.0138` n `6`; index avg `0.0543` n `27`; metal avg `-0.0539` n `20`; unknown avg `158.5593` n `1264`
- 4h: commodity avg `0.2016` n `13`; crypto_alt avg `-0.4454` n `239`; crypto_major avg `-0.6483` n `8`; equity avg `-0.6292` n `162`; fx avg `-0.0802` n `6`; index avg `-0.0329` n `27`; metal avg `-0.169` n `20`; unknown avg `0.1818` n `1188`
- 24h: commodity avg `-0.8817` n `13`; crypto_alt avg `0.3674` n `239`; crypto_major avg `0.5495` n `8`; equity avg `-3.0085` n `162`; fx avg `-0.0852` n `6`; index avg `-0.3063` n `27`; metal avg `-0.2025` n `20`; unknown avg `17.3034` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
