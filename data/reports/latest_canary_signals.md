# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T19:52:44.577830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `0.0389` n `236`; crypto_major avg `0.1297` n `8`; equity avg `0.0282` n `151`; fx avg `0.0032` n `6`; index avg `0.0051` n `26`; metal avg `0.0956` n `20`; unknown avg `0.7358` n `1104`
- 1h: commodity avg `-0.0389` n `13`; crypto_alt avg `0.2215` n `236`; crypto_major avg `0.1606` n `8`; equity avg `1.0366` n `151`; fx avg `-0.0049` n `6`; index avg `0.136` n `26`; metal avg `0.1103` n `20`; unknown avg `2.1429` n `1102`
- 4h: commodity avg `-0.1126` n `13`; crypto_alt avg `0.7615` n `236`; crypto_major avg `0.2894` n `8`; equity avg `1.3905` n `151`; fx avg `-0.0002` n `6`; index avg `0.163` n `26`; metal avg `0.1351` n `20`; unknown avg `0.4258` n `1096`
- 24h: commodity avg `-0.2285` n `13`; crypto_alt avg `1.2` n `236`; crypto_major avg `0.6857` n `8`; equity avg `-0.0044` n `151`; fx avg `0.1799` n `6`; index avg `-0.0788` n `26`; metal avg `0.5483` n `20`; unknown avg `11.574` n `916`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0978`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0845`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0782`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0714`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0657`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0494`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
