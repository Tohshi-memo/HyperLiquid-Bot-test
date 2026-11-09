# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T07:07:24.710791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3339` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.146` n `13`; crypto_alt avg `-0.5827` n `239`; crypto_major avg `-0.4965` n `8`; equity avg `-0.2618` n `158`; fx avg `-0.012` n `6`; index avg `-0.0326` n `27`; metal avg `-0.056` n `20`; unknown avg `3.5478` n `1259`
- 1h: commodity avg `-0.082` n `13`; crypto_alt avg `-0.8311` n `239`; crypto_major avg `-0.8928` n `8`; equity avg `-0.6854` n `158`; fx avg `-0.0411` n `6`; index avg `-0.0751` n `27`; metal avg `-0.1576` n `20`; unknown avg `7.255` n `1255`
- 4h: commodity avg `-0.2453` n `13`; crypto_alt avg `-1.4015` n `239`; crypto_major avg `-1.5091` n `8`; equity avg `-1.4662` n `158`; fx avg `-0.0905` n `6`; index avg `-0.1752` n `27`; metal avg `-0.1853` n `20`; unknown avg `8.3049` n `1208`
- 24h: commodity avg `-0.1123` n `13`; crypto_alt avg `-2.9135` n `239`; crypto_major avg `-3.7227` n `8`; equity avg `-0.8314` n `158`; fx avg `-0.1768` n `6`; index avg `-0.099` n `27`; metal avg `0.2678` n `20`; unknown avg `1.5249` n `982`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
