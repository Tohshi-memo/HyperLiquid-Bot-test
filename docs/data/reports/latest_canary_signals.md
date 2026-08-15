# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T13:22:29.420479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.0413` n `230`; crypto_major avg `-0.0214` n `8`; equity avg `0.0141` n `114`; fx avg `0.0011` n `6`; index avg `0.0049` n `25`; metal avg `-0.0047` n `20`; unknown avg `-0.0395` n `791`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.1041` n `230`; crypto_major avg `0.1631` n `8`; equity avg `0.0132` n `114`; fx avg `0.0008` n `6`; index avg `0.0025` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0144` n `791`
- 4h: commodity avg `0.028` n `12`; crypto_alt avg `-0.0644` n `230`; crypto_major avg `0.1641` n `8`; equity avg `0.0447` n `114`; fx avg `-0.0115` n `6`; index avg `0.006` n `25`; metal avg `-0.0132` n `20`; unknown avg `-0.0595` n `791`
- 24h: commodity avg `0.0775` n `12`; crypto_alt avg `1.1199` n `230`; crypto_major avg `0.5196` n `8`; equity avg `-0.4891` n `114`; fx avg `0.1238` n `6`; index avg `-0.1103` n `25`; metal avg `0.0578` n `20`; unknown avg `-0.1063` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
