# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T13:37:26.075090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0774` n `13`; crypto_alt avg `-0.4066` n `239`; crypto_major avg `-0.3182` n `8`; equity avg `-0.0475` n `158`; fx avg `-0.0095` n `6`; index avg `-0.0017` n `27`; metal avg `-0.0028` n `20`; unknown avg `2.8179` n `1262`
- 1h: commodity avg `0.002` n `13`; crypto_alt avg `-0.1856` n `239`; crypto_major avg `0.0748` n `8`; equity avg `0.0612` n `158`; fx avg `-0.0014` n `6`; index avg `0.0024` n `27`; metal avg `-0.0057` n `20`; unknown avg `1.1565` n `1256`
- 4h: commodity avg `0.0074` n `13`; crypto_alt avg `-0.3039` n `239`; crypto_major avg `0.2186` n `8`; equity avg `0.1385` n `158`; fx avg `-0.0028` n `6`; index avg `0.0171` n `27`; metal avg `-0.0076` n `20`; unknown avg `208.2341` n `1234`
- 24h: commodity avg `0.1001` n `13`; crypto_alt avg `-1.7798` n `239`; crypto_major avg `-0.1732` n `8`; equity avg `0.1345` n `158`; fx avg `0.0004` n `6`; index avg `0.0089` n `27`; metal avg `-0.0384` n `20`; unknown avg `6.3476` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
