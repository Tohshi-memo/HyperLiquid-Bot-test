# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T19:52:37.591011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.4487` n `234`; crypto_major avg `-0.4552` n `8`; equity avg `-0.0634` n `142`; fx avg `-0.0015` n `6`; index avg `-0.0305` n `26`; metal avg `-0.0106` n `20`; unknown avg `136.4866` n `969`
- 1h: commodity avg `-0.0668` n `12`; crypto_alt avg `-0.4051` n `234`; crypto_major avg `-0.5213` n `8`; equity avg `0.0242` n `142`; fx avg `0.0107` n `6`; index avg `-0.0147` n `26`; metal avg `0.0381` n `20`; unknown avg `23.6508` n `967`
- 4h: commodity avg `-0.1889` n `12`; crypto_alt avg `-1.2921` n `234`; crypto_major avg `-0.6691` n `8`; equity avg `-0.1539` n `142`; fx avg `-0.0155` n `6`; index avg `-0.11` n `26`; metal avg `0.0425` n `20`; unknown avg `15.0151` n `961`
- 24h: commodity avg `0.3294` n `12`; crypto_alt avg `-0.0428` n `234`; crypto_major avg `0.3658` n `8`; equity avg `-0.2126` n `142`; fx avg `0.0582` n `6`; index avg `-0.008` n `26`; metal avg `-0.1793` n `20`; unknown avg `10.95` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
