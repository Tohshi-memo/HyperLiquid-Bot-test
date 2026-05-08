# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T06:22:11.676328+00:00`
- Correlation status: `ready`
- Asset price records: `621`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `0.3365` n `228`; crypto_major avg `0.0677` n `8`; equity avg `0.1299` n `65`; fx avg `0.0191` n `5`; index avg `0.0457` n `23`; metal avg `-0.1426` n `18`; unknown avg `-0.115` n `375`
- 1h: commodity avg `-0.3049` n `12`; crypto_alt avg `-0.0149` n `228`; crypto_major avg `-0.0744` n `8`; equity avg `0.07` n `65`; fx avg `0.0667` n `5`; index avg `0.0836` n `23`; metal avg `0.4231` n `18`; unknown avg `0.0472` n `355`
- 4h: commodity avg `-0.3601` n `12`; crypto_alt avg `0.7243` n `228`; crypto_major avg `0.1411` n `8`; equity avg `0.4094` n `65`; fx avg `0.1021` n `5`; index avg `0.1853` n `23`; metal avg `0.5649` n `18`; unknown avg `-0.114` n `355`
- 24h: commodity avg `0.1819` n `12`; crypto_alt avg `1.511` n `228`; crypto_major avg `-1.5692` n `8`; equity avg `-0.9117` n `65`; fx avg `0.2387` n `5`; index avg `-0.5642` n `23`; metal avg `0.5929` n `18`; unknown avg `-0.145` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1273`, n `613`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1271`, n `613`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `617`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `617`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `617`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `617`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `613`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.082`, n `613`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0811`, n `613`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `617`, weak_sample_signal
