# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T21:37:17.359053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0685` n `12`; crypto_alt avg `0.1624` n `228`; crypto_major avg `0.0167` n `8`; equity avg `0.0145` n `67`; fx avg `-0.0171` n `6`; index avg `0.0563` n `23`; metal avg `-0.0084` n `18`; unknown avg `-0.2818` n `418`
- 1h: commodity avg `0.1749` n `12`; crypto_alt avg `0.1942` n `228`; crypto_major avg `-0.0773` n `8`; equity avg `0.1349` n `67`; fx avg `-0.0203` n `6`; index avg `0.0031` n `23`; metal avg `-0.0215` n `18`; unknown avg `-0.2896` n `418`
- 4h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.1252` n `228`; crypto_major avg `-0.3177` n `8`; equity avg `0.0448` n `67`; fx avg `0.0085` n `6`; index avg `0.1636` n `23`; metal avg `0.5446` n `18`; unknown avg `-0.7193` n `418`
- 24h: commodity avg `0.6055` n `12`; crypto_alt avg `-1.7784` n `228`; crypto_major avg `-1.5473` n `8`; equity avg `-0.3292` n `67`; fx avg `-0.1334` n `6`; index avg `0.3728` n `23`; metal avg `-0.8987` n `18`; unknown avg `0.1564` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
