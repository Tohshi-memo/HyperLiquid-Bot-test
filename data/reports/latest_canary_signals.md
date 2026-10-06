# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T15:07:35.501803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `13`; crypto_alt avg `-0.0122` n `235`; crypto_major avg `0.0718` n `8`; equity avg `0.197` n `150`; fx avg `0.0042` n `6`; index avg `0.0232` n `26`; metal avg `0.0906` n `20`; unknown avg `-0.0747` n `1070`
- 1h: commodity avg `-0.0331` n `13`; crypto_alt avg `0.5747` n `235`; crypto_major avg `0.4629` n `8`; equity avg `0.117` n `150`; fx avg `-0.0022` n `6`; index avg `-0.017` n `26`; metal avg `0.0539` n `20`; unknown avg `5.1348` n `1024`
- 4h: commodity avg `0.1381` n `13`; crypto_alt avg `0.2454` n `235`; crypto_major avg `0.4427` n `8`; equity avg `0.6517` n `150`; fx avg `0.0303` n `6`; index avg `0.0661` n `26`; metal avg `0.0206` n `20`; unknown avg `4.5402` n `1018`
- 24h: commodity avg `-0.6581` n `13`; crypto_alt avg `0.6275` n `235`; crypto_major avg `0.6977` n `8`; equity avg `1.1252` n `149`; fx avg `0.082` n `6`; index avg `0.1829` n `26`; metal avg `-0.0698` n `20`; unknown avg `381.2836` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
