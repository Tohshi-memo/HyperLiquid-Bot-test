# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T01:07:31.432786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1055` n `13`; crypto_alt avg `-0.4439` n `237`; crypto_major avg `-0.39` n `8`; equity avg `-0.3424` n `151`; fx avg `0.0221` n `6`; index avg `-0.0902` n `26`; metal avg `-0.122` n `20`; unknown avg `0.5609` n `1197`
- 1h: commodity avg `0.079` n `13`; crypto_alt avg `-0.1271` n `237`; crypto_major avg `-0.0065` n `8`; equity avg `0.0256` n `151`; fx avg `0.0262` n `6`; index avg `-0.0303` n `26`; metal avg `-0.1163` n `20`; unknown avg `0.5441` n `1197`
- 4h: commodity avg `0.1264` n `13`; crypto_alt avg `-0.2476` n `237`; crypto_major avg `-0.0661` n `8`; equity avg `0.3294` n `151`; fx avg `0.0159` n `6`; index avg `-0.04` n `26`; metal avg `-0.1566` n `20`; unknown avg `0.5746` n `1085`
- 24h: commodity avg `-0.0031` n `13`; crypto_alt avg `2.8572` n `237`; crypto_major avg `2.168` n `8`; equity avg `2.5364` n `151`; fx avg `0.0563` n `6`; index avg `0.2797` n `26`; metal avg `0.049` n `20`; unknown avg `212.3098` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
