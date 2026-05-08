# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T01:07:17.999429+00:00`
- Correlation status: `ready`
- Asset price records: `600`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.248` n `12`; crypto_alt avg `0.1385` n `228`; crypto_major avg `-0.0015` n `8`; equity avg `0.1428` n `65`; fx avg `-0.0004` n `5`; index avg `0.0974` n `23`; metal avg `0.6151` n `18`; unknown avg `0.103` n `365`
- 1h: commodity avg `-0.0704` n `12`; crypto_alt avg `-0.2395` n `228`; crypto_major avg `-0.3124` n `8`; equity avg `0.2791` n `65`; fx avg `0.0571` n `5`; index avg `0.1225` n `23`; metal avg `0.3523` n `18`; unknown avg `-0.0624` n `365`
- 4h: commodity avg `-0.6666` n `12`; crypto_alt avg `0.6614` n `228`; crypto_major avg `-0.0261` n `8`; equity avg `0.3505` n `65`; fx avg `0.106` n `5`; index avg `0.312` n `23`; metal avg `0.862` n `18`; unknown avg `-0.1738` n `365`
- 24h: commodity avg `0.3905` n `12`; crypto_alt avg `2.2665` n `228`; crypto_major avg `-1.2635` n `8`; equity avg `-0.5218` n `65`; fx avg `0.1802` n `5`; index avg `-0.4802` n `23`; metal avg `0.4662` n `18`; unknown avg `-0.1405` n `354`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1363`, n `596`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `596`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `596`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1061`, n `592`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1043`, n `592`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `596`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `592`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `592`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.081`, n `592`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `596`, weak_sample_signal
