# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T09:22:30.430738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1287` n `12`; crypto_alt avg `-0.2027` n `234`; crypto_major avg `-0.1175` n `8`; equity avg `-0.0026` n `141`; fx avg `-0.0157` n `6`; index avg `-0.009` n `26`; metal avg `-0.0161` n `20`; unknown avg `0.3597` n `946`
- 1h: commodity avg `-0.1219` n `12`; crypto_alt avg `0.1246` n `234`; crypto_major avg `0.2018` n `8`; equity avg `0.2231` n `141`; fx avg `-0.0529` n `6`; index avg `0.0456` n `26`; metal avg `0.1122` n `20`; unknown avg `0.6863` n `944`
- 4h: commodity avg `-0.1523` n `12`; crypto_alt avg `1.619` n `234`; crypto_major avg `0.9697` n `8`; equity avg `0.6208` n `141`; fx avg `-0.0539` n `6`; index avg `0.1254` n `26`; metal avg `0.2631` n `20`; unknown avg `3.7697` n `904`
- 24h: commodity avg `-0.0175` n `12`; crypto_alt avg `4.8856` n `234`; crypto_major avg `2.6045` n `8`; equity avg `2.2068` n `141`; fx avg `-0.2435` n `6`; index avg `0.3265` n `26`; metal avg `0.1631` n `20`; unknown avg `17.4223` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
