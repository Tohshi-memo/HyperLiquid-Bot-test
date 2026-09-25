# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T22:37:28.670319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.3932` n `234`; crypto_major avg `0.2855` n `8`; equity avg `0.0037` n `141`; fx avg `0.004` n `6`; index avg `0.0018` n `26`; metal avg `0.0032` n `20`; unknown avg `0.449` n `960`
- 1h: commodity avg `0.0492` n `12`; crypto_alt avg `1.117` n `234`; crypto_major avg `0.8065` n `8`; equity avg `0.0157` n `141`; fx avg `0.0126` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0134` n `20`; unknown avg `0.7665` n `932`
- 4h: commodity avg `0.127` n `12`; crypto_alt avg `0.7418` n `234`; crypto_major avg `0.3514` n `8`; equity avg `-0.0133` n `141`; fx avg `-0.0074` n `6`; index avg `0.0307` n `26`; metal avg `-0.0174` n `20`; unknown avg `0.3831` n `852`
- 24h: commodity avg `-0.4138` n `12`; crypto_alt avg `3.001` n `234`; crypto_major avg `1.4797` n `8`; equity avg `0.1504` n `141`; fx avg `-0.2288` n `6`; index avg `0.2529` n `26`; metal avg `0.1683` n `20`; unknown avg `1124.4569` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
