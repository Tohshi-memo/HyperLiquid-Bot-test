# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T17:22:36.772936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `0.0745` n `237`; crypto_major avg `-0.0368` n `8`; equity avg `-0.0988` n `152`; fx avg `-0.0065` n `6`; index avg `-0.0275` n `26`; metal avg `-0.0478` n `20`; unknown avg `-0.2796` n `1231`
- 1h: commodity avg `-0.1094` n `13`; crypto_alt avg `0.0555` n `237`; crypto_major avg `0.1246` n `8`; equity avg `-0.0652` n `152`; fx avg `-0.0209` n `6`; index avg `-0.0564` n `26`; metal avg `-0.107` n `20`; unknown avg `0.0792` n `1203`
- 4h: commodity avg `0.2145` n `13`; crypto_alt avg `0.1923` n `237`; crypto_major avg `0.0962` n `8`; equity avg `0.479` n `152`; fx avg `0.0252` n `6`; index avg `0.0875` n `26`; metal avg `-0.1096` n `20`; unknown avg `-0.3282` n `1149`
- 24h: commodity avg `0.3711` n `13`; crypto_alt avg `1.1764` n `237`; crypto_major avg `1.0419` n `8`; equity avg `1.2316` n `152`; fx avg `-0.1184` n `6`; index avg `0.0055` n `26`; metal avg `-0.2741` n `20`; unknown avg `-0.5725` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
