# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T20:22:32.525508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `13`; crypto_alt avg `-0.1171` n `237`; crypto_major avg `-0.0882` n `8`; equity avg `-0.1821` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0289` n `26`; metal avg `-0.0265` n `20`; unknown avg `1.0432` n `1195`
- 1h: commodity avg `-0.0246` n `13`; crypto_alt avg `-0.2722` n `237`; crypto_major avg `-0.2556` n `8`; equity avg `0.0561` n `151`; fx avg `-0.0166` n `6`; index avg `0.0046` n `26`; metal avg `-0.0396` n `20`; unknown avg `1.0991` n `1179`
- 4h: commodity avg `0.1492` n `13`; crypto_alt avg `-0.4604` n `237`; crypto_major avg `-0.6485` n `8`; equity avg `-1.0334` n `151`; fx avg `-0.0301` n `6`; index avg `-0.1428` n `26`; metal avg `-0.1636` n `20`; unknown avg `0.6084` n `1179`
- 24h: commodity avg `0.5547` n `13`; crypto_alt avg `-5.4027` n `237`; crypto_major avg `-4.0136` n `8`; equity avg `-5.6584` n `151`; fx avg `-0.1823` n `6`; index avg `-0.6767` n `26`; metal avg `-0.9999` n `20`; unknown avg `60.0022` n `934`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
