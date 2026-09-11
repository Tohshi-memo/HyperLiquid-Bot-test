# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T20:22:32.474115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.2263` n `233`; crypto_major avg `-0.1476` n `8`; equity avg `-0.009` n `136`; fx avg `-0.0109` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0087` n `20`; unknown avg `0.5725` n `810`
- 1h: commodity avg `-0.0465` n `12`; crypto_alt avg `0.4131` n `233`; crypto_major avg `0.4517` n `8`; equity avg `-0.0009` n `136`; fx avg `-0.0146` n `6`; index avg `-0.0046` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.3086` n `796`
- 4h: commodity avg `0.0581` n `12`; crypto_alt avg `-0.5687` n `233`; crypto_major avg `-0.2533` n `8`; equity avg `-0.1762` n `136`; fx avg `0.0019` n `6`; index avg `-0.0224` n `26`; metal avg `0.0063` n `20`; unknown avg `-0.3707` n `726`
- 24h: commodity avg `-0.5677` n `12`; crypto_alt avg `0.1686` n `233`; crypto_major avg `0.9799` n `8`; equity avg `0.6083` n `136`; fx avg `-0.158` n `6`; index avg `0.2914` n `26`; metal avg `0.2986` n `20`; unknown avg `1.1067` n `670`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
