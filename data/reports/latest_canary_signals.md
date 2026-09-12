# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T04:52:27.025302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.0925` n `233`; crypto_major avg `-0.1005` n `8`; equity avg `-0.0107` n `136`; fx avg `0.002` n `6`; index avg `-0.0007` n `26`; metal avg `-0.004` n `20`; unknown avg `2.1374` n `840`
- 1h: commodity avg `-0.0622` n `12`; crypto_alt avg `0.0174` n `233`; crypto_major avg `-0.0069` n `8`; equity avg `-0.0135` n `136`; fx avg `0.0009` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0003` n `20`; unknown avg `1.6734` n `830`
- 4h: commodity avg `-0.1089` n `12`; crypto_alt avg `0.3286` n `233`; crypto_major avg `0.1683` n `8`; equity avg `-0.0574` n `136`; fx avg `0.0187` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0364` n `20`; unknown avg `8.9922` n `814`
- 24h: commodity avg `-0.6264` n `12`; crypto_alt avg `0.7776` n `233`; crypto_major avg `0.8789` n `8`; equity avg `0.8033` n `136`; fx avg `-0.1087` n `6`; index avg `0.2376` n `26`; metal avg `0.1367` n `20`; unknown avg `1.6317` n `690`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
