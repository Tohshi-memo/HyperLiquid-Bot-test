# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T18:37:32.238529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `13`; crypto_alt avg `-0.0587` n `235`; crypto_major avg `-0.0187` n `8`; equity avg `-0.0863` n `151`; fx avg `0.0028` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0159` n `20`; unknown avg `1.2094` n `1135`
- 1h: commodity avg `0.0386` n `13`; crypto_alt avg `-0.0829` n `235`; crypto_major avg `-0.0886` n `8`; equity avg `0.0814` n `151`; fx avg `0.017` n `6`; index avg `0.0213` n `26`; metal avg `0.0106` n `20`; unknown avg `1.4212` n `1133`
- 4h: commodity avg `0.2178` n `13`; crypto_alt avg `-0.3758` n `235`; crypto_major avg `-0.4619` n `8`; equity avg `0.1637` n `151`; fx avg `0.0208` n `6`; index avg `0.0106` n `26`; metal avg `-0.0687` n `20`; unknown avg `2.4387` n `1123`
- 24h: commodity avg `0.4738` n `13`; crypto_alt avg `-1.6224` n `235`; crypto_major avg `-0.3687` n `8`; equity avg `-0.9061` n `151`; fx avg `0.1759` n `6`; index avg `-0.1687` n `26`; metal avg `-0.2425` n `20`; unknown avg `1.1201` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1632`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1471`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0919`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
