# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T21:07:27.469614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `-0.0538` n `239`; crypto_major avg `0.0218` n `8`; equity avg `-0.0384` n `158`; fx avg `0.0007` n `6`; index avg `0.0078` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.4803` n `1238`
- 1h: commodity avg `0.0592` n `13`; crypto_alt avg `-0.8134` n `239`; crypto_major avg `-0.4862` n `8`; equity avg `-0.1343` n `158`; fx avg `-0.0049` n `6`; index avg `0.0003` n `27`; metal avg `-0.0079` n `20`; unknown avg `-0.102` n `1228`
- 4h: commodity avg `0.0445` n `13`; crypto_alt avg `-0.7193` n `239`; crypto_major avg `-0.4039` n `8`; equity avg `-0.0514` n `158`; fx avg `-0.0042` n `6`; index avg `0.0093` n `27`; metal avg `-0.0057` n `20`; unknown avg `0.2861` n `1194`
- 24h: commodity avg `0.1421` n `13`; crypto_alt avg `-2.1817` n `239`; crypto_major avg `-0.9553` n `8`; equity avg `-0.1991` n `158`; fx avg `-0.0134` n `6`; index avg `0.0347` n `27`; metal avg `-0.0053` n `20`; unknown avg `-0.3301` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
