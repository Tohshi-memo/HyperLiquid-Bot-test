# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T02:52:25.851114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.98` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.057` n `233`; crypto_major avg `-0.0347` n `8`; equity avg `0.0091` n `136`; fx avg `0.0031` n `6`; index avg `0.0007` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.0319` n `838`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `0.0732` n `233`; crypto_major avg `-0.0213` n `8`; equity avg `-0.0193` n `136`; fx avg `0.0008` n `6`; index avg `0.0003` n `26`; metal avg `0.0008` n `20`; unknown avg `4.1684` n `836`
- 4h: commodity avg `-0.1122` n `12`; crypto_alt avg `1.2851` n `233`; crypto_major avg `0.3936` n `8`; equity avg `0.1328` n `136`; fx avg `-0.0026` n `6`; index avg `0.0137` n `26`; metal avg `-0.0234` n `20`; unknown avg `0.7999` n `820`
- 24h: commodity avg `-0.6401` n `12`; crypto_alt avg `1.6461` n `233`; crypto_major avg `1.3767` n `8`; equity avg `1.0804` n `136`; fx avg `-0.1337` n `6`; index avg `0.3269` n `26`; metal avg `0.2409` n `20`; unknown avg `30.2211` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
