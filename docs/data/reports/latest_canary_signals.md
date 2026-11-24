# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T16:22:31.840497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4368` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0856` n `13`; crypto_alt avg `-0.0234` n `239`; crypto_major avg `0.1232` n `8`; equity avg `0.2127` n `168`; fx avg `0.0334` n `6`; index avg `0.0459` n `27`; metal avg `0.0866` n `20`; unknown avg `0.0005` n `1259`
- 1h: commodity avg `-0.0479` n `13`; crypto_alt avg `-0.1658` n `239`; crypto_major avg `0.0591` n `8`; equity avg `-0.7697` n `168`; fx avg `0.0379` n `6`; index avg `-0.0705` n `27`; metal avg `-0.3117` n `20`; unknown avg `0.18` n `1255`
- 4h: commodity avg `0.2362` n `13`; crypto_alt avg `-1.668` n `239`; crypto_major avg `-1.5763` n `8`; equity avg `-2.2347` n `168`; fx avg `0.0728` n `6`; index avg `-0.1395` n `27`; metal avg `-0.5666` n `20`; unknown avg `-0.3726` n `1243`
- 24h: commodity avg `0.5561` n `13`; crypto_alt avg `-5.5964` n `239`; crypto_major avg `-5.5322` n `8`; equity avg `-5.4999` n `167`; fx avg `0.2522` n `6`; index avg `-0.4422` n `27`; metal avg `-1.3552` n `20`; unknown avg `174.2493` n `1139`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
