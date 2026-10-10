# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T20:37:26.770408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `13`; crypto_alt avg `0.1074` n `235`; crypto_major avg `0.0459` n `8`; equity avg `-0.0022` n `150`; fx avg `0.0012` n `6`; index avg `0.0041` n `26`; metal avg `0.0063` n `20`; unknown avg `9.9832` n `1117`
- 1h: commodity avg `-0.0005` n `13`; crypto_alt avg `0.0568` n `235`; crypto_major avg `-0.1376` n `8`; equity avg `-0.0035` n `150`; fx avg `0.0004` n `6`; index avg `0.0111` n `26`; metal avg `0.0026` n `20`; unknown avg `3.7955` n `1101`
- 4h: commodity avg `0.021` n `13`; crypto_alt avg `0.3547` n `235`; crypto_major avg `0.0043` n `8`; equity avg `-0.0013` n `150`; fx avg `-0.004` n `6`; index avg `-0.007` n `26`; metal avg `-0.0` n `20`; unknown avg `1.7113` n `999`
- 24h: commodity avg `-0.1701` n `13`; crypto_alt avg `3.2345` n `235`; crypto_major avg `1.2654` n `8`; equity avg `0.182` n `150`; fx avg `-0.0049` n `6`; index avg `0.0282` n `26`; metal avg `-0.0235` n `20`; unknown avg `1.8794` n `964`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
