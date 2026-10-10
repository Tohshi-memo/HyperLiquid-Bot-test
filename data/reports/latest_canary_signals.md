# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T01:37:25.319477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `13`; crypto_alt avg `0.0283` n `235`; crypto_major avg `0.0111` n `8`; equity avg `0.0081` n `150`; fx avg `-0.0015` n `6`; index avg `0.0004` n `26`; metal avg `-0.0066` n `20`; unknown avg `-0.049` n `1116`
- 1h: commodity avg `0.0125` n `13`; crypto_alt avg `-0.0891` n `235`; crypto_major avg `0.0334` n `8`; equity avg `0.0179` n `150`; fx avg `0.0008` n `6`; index avg `0.0075` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.0268` n `1114`
- 4h: commodity avg `0.0002` n `13`; crypto_alt avg `1.043` n `235`; crypto_major avg `0.3352` n `8`; equity avg `0.0846` n `150`; fx avg `0.0028` n `6`; index avg `0.0243` n `26`; metal avg `0.0094` n `20`; unknown avg `0.0913` n `1108`
- 24h: commodity avg `-0.1132` n `13`; crypto_alt avg `2.4274` n `235`; crypto_major avg `0.6719` n `8`; equity avg `0.708` n `150`; fx avg `-0.012` n `6`; index avg `0.1334` n `26`; metal avg `0.2332` n `20`; unknown avg `13.1658` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
