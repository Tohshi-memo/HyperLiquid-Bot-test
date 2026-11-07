# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T06:37:30.243381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `13`; crypto_alt avg `0.0863` n `239`; crypto_major avg `-0.0031` n `8`; equity avg `-0.0137` n `158`; fx avg `0.0078` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0042` n `20`; unknown avg `0.1417` n `1259`
- 1h: commodity avg `-0.021` n `13`; crypto_alt avg `-0.0544` n `239`; crypto_major avg `0.0587` n `8`; equity avg `-0.0941` n `158`; fx avg `-0.0095` n `6`; index avg `-0.0023` n `27`; metal avg `-0.0148` n `20`; unknown avg `0.0565` n `1227`
- 4h: commodity avg `-0.075` n `13`; crypto_alt avg `-0.2102` n `239`; crypto_major avg `-0.1895` n `8`; equity avg `-0.1004` n `158`; fx avg `-0.0152` n `6`; index avg `0.0045` n `27`; metal avg `-0.0115` n `20`; unknown avg `0.1527` n `1205`
- 24h: commodity avg `-0.3733` n `13`; crypto_alt avg `0.0755` n `239`; crypto_major avg `0.1274` n `8`; equity avg `1.1963` n `158`; fx avg `-0.0411` n `6`; index avg `0.2028` n `27`; metal avg `0.2134` n `20`; unknown avg `8.4416` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
