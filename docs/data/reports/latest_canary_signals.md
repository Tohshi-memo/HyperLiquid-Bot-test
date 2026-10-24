# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T12:06:06.470888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0428` n `13`; crypto_alt avg `-0.0984` n `237`; crypto_major avg `-0.0575` n `8`; equity avg `-0.0078` n `152`; fx avg `0.0056` n `6`; index avg `-0.0006` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.1187` n `1222`
- 1h: commodity avg `0.1088` n `13`; crypto_alt avg `-0.2333` n `237`; crypto_major avg `-0.1003` n `8`; equity avg `-0.01` n `152`; fx avg `-0.008` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0004` n `20`; unknown avg `-0.0422` n `1224`
- 4h: commodity avg `0.1327` n `13`; crypto_alt avg `-0.178` n `237`; crypto_major avg `-0.3028` n `8`; equity avg `-0.0317` n `152`; fx avg `0.0071` n `6`; index avg `-0.0226` n `26`; metal avg `-0.025` n `20`; unknown avg `118.075` n `1206`
- 24h: commodity avg `0.2997` n `13`; crypto_alt avg `-2.7866` n `237`; crypto_major avg `-2.0937` n `8`; equity avg `-0.3452` n `152`; fx avg `0.0195` n `6`; index avg `0.0199` n `26`; metal avg `-0.2053` n `20`; unknown avg `193.8739` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1981`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
