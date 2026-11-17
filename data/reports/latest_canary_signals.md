# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T13:37:25.739343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0335` n `13`; crypto_alt avg `-0.2285` n `239`; crypto_major avg `-0.1095` n `8`; equity avg `-0.131` n `162`; fx avg `-0.0129` n `6`; index avg `-0.0147` n `27`; metal avg `-0.0606` n `20`; unknown avg `1.7257` n `1266`
- 1h: commodity avg `0.0572` n `13`; crypto_alt avg `-0.0725` n `239`; crypto_major avg `0.1283` n `8`; equity avg `-0.6106` n `162`; fx avg `-0.0167` n `6`; index avg `-0.0579` n `27`; metal avg `-0.1354` n `20`; unknown avg `4.5622` n `1224`
- 4h: commodity avg `0.1563` n `13`; crypto_alt avg `1.1739` n `239`; crypto_major avg `1.0507` n `8`; equity avg `1.615` n `162`; fx avg `-0.0035` n `6`; index avg `0.1242` n `27`; metal avg `-0.0635` n `20`; unknown avg `167.0145` n `1216`
- 24h: commodity avg `-0.4121` n `13`; crypto_alt avg `2.3321` n `239`; crypto_major avg `2.4234` n `8`; equity avg `-0.9903` n `162`; fx avg `-0.0847` n `6`; index avg `-0.1428` n `27`; metal avg `-0.2474` n `20`; unknown avg `13.8292` n `1103`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
