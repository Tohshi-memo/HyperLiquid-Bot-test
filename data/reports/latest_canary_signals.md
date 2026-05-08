# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T06:25:08.179936+00:00`
- Correlation status: `ready`
- Asset price records: `621`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0188` n `12`; crypto_alt avg `0.1876` n `228`; crypto_major avg `-0.0202` n `8`; equity avg `0.1273` n `65`; fx avg `0.0259` n `5`; index avg `0.0463` n `23`; metal avg `-0.1231` n `18`; unknown avg `-0.1583` n `375`
- 1h: commodity avg `-0.3078` n `12`; crypto_alt avg `-0.163` n `228`; crypto_major avg `-0.1621` n `8`; equity avg `0.0674` n `65`; fx avg `0.0735` n `5`; index avg `0.0843` n `23`; metal avg `0.4429` n `18`; unknown avg `0.0117` n `355`
- 4h: commodity avg `-0.363` n `12`; crypto_alt avg `0.5753` n `228`; crypto_major avg `0.0531` n `8`; equity avg `0.4068` n `65`; fx avg `0.1089` n `5`; index avg `0.186` n `23`; metal avg `0.5847` n `18`; unknown avg `-0.149` n `355`
- 24h: commodity avg `0.179` n `12`; crypto_alt avg `1.3619` n `228`; crypto_major avg `-1.6554` n `8`; equity avg `-0.9146` n `65`; fx avg `0.2456` n `5`; index avg `-0.5635` n `23`; metal avg `0.6128` n `18`; unknown avg `-0.1809` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1278`, n `613`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1275`, n `613`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `617`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `617`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `617`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `617`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `613`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.082`, n `613`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0811`, n `613`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0711`, n `617`, weak_sample_signal
