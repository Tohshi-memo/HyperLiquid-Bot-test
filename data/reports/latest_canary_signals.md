# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T02:52:26.416654+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0691` n `13`; crypto_alt avg `-0.2547` n `239`; crypto_major avg `-0.3725` n `8`; equity avg `-0.3579` n `162`; fx avg `-0.0073` n `6`; index avg `-0.0509` n `27`; metal avg `-0.0886` n `20`; unknown avg `0.2592` n `1265`
- 1h: commodity avg `-0.1014` n `13`; crypto_alt avg `1.0619` n `239`; crypto_major avg `0.6186` n `8`; equity avg `0.4197` n `162`; fx avg `-0.0092` n `6`; index avg `0.0112` n `27`; metal avg `0.0315` n `20`; unknown avg `0.0305` n `1259`
- 4h: commodity avg `-0.343` n `13`; crypto_alt avg `-0.0211` n `239`; crypto_major avg `-0.4441` n `8`; equity avg `-0.349` n `162`; fx avg `-0.0289` n `6`; index avg `-0.0503` n `27`; metal avg `-0.1257` n `20`; unknown avg `0.4625` n `1239`
- 24h: commodity avg `-0.455` n `13`; crypto_alt avg `0.5717` n `239`; crypto_major avg `0.6912` n `8`; equity avg `0.4552` n `162`; fx avg `-0.0197` n `6`; index avg `0.0407` n `27`; metal avg `0.1262` n `20`; unknown avg `0.7304` n `1125`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
