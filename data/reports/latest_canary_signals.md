# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T02:37:31.579633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `-0.1056` n `234`; crypto_major avg `-0.027` n `8`; equity avg `-0.0898` n `141`; fx avg `-0.0255` n `6`; index avg `-0.0176` n `26`; metal avg `-0.0178` n `20`; unknown avg `1.7315` n `963`
- 1h: commodity avg `-0.076` n `12`; crypto_alt avg `-0.5569` n `234`; crypto_major avg `-0.0335` n `8`; equity avg `-0.0583` n `141`; fx avg `-0.0364` n `6`; index avg `-0.0138` n `26`; metal avg `0.0269` n `20`; unknown avg `2.0101` n `961`
- 4h: commodity avg `0.0139` n `12`; crypto_alt avg `-1.6629` n `234`; crypto_major avg `-1.0079` n `8`; equity avg `-0.3869` n `141`; fx avg `-0.0487` n `6`; index avg `-0.0643` n `26`; metal avg `-0.0308` n `20`; unknown avg `1.8535` n `955`
- 24h: commodity avg `0.1059` n `12`; crypto_alt avg `-4.5145` n `234`; crypto_major avg `-1.9621` n `8`; equity avg `-2.149` n `141`; fx avg `-0.0748` n `6`; index avg `-0.1905` n `26`; metal avg `-0.4995` n `20`; unknown avg `7.8539` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
