# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T17:07:27.995751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `13`; crypto_alt avg `-0.1853` n `235`; crypto_major avg `-0.0446` n `8`; equity avg `0.0015` n `150`; fx avg `0.0` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0029` n `20`; unknown avg `14.8666` n `1107`
- 1h: commodity avg `-0.0368` n `13`; crypto_alt avg `-0.0001` n `235`; crypto_major avg `-0.1417` n `8`; equity avg `-0.0349` n `150`; fx avg `0.0` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0059` n `20`; unknown avg `19.7553` n `1107`
- 4h: commodity avg `-0.0244` n `13`; crypto_alt avg `0.9463` n `235`; crypto_major avg `0.3309` n `8`; equity avg `0.0761` n `150`; fx avg `-0.0076` n `6`; index avg `0.0053` n `26`; metal avg `-0.0092` n `20`; unknown avg `1.0276` n `1093`
- 24h: commodity avg `-0.343` n `13`; crypto_alt avg `2.3291` n `235`; crypto_major avg `0.7651` n `8`; equity avg `0.2821` n `150`; fx avg `0.013` n `6`; index avg `0.0373` n `26`; metal avg `0.0213` n `20`; unknown avg `1.6038` n `984`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
