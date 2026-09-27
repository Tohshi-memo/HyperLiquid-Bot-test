# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T02:53:02.071124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `-0.1367` n `234`; crypto_major avg `-0.0647` n `8`; equity avg `-0.0005` n `141`; fx avg `-0.0021` n `6`; index avg `0.0018` n `26`; metal avg `-0.0019` n `20`; unknown avg `-0.0046` n `961`
- 1h: commodity avg `0.0381` n `12`; crypto_alt avg `-0.1676` n `234`; crypto_major avg `-0.0488` n `8`; equity avg `0.0338` n `141`; fx avg `-0.0053` n `6`; index avg `0.0029` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.6399` n `955`
- 4h: commodity avg `-0.0531` n `12`; crypto_alt avg `0.0806` n `234`; crypto_major avg `0.2344` n `8`; equity avg `0.0779` n `141`; fx avg `-0.0072` n `6`; index avg `0.0037` n `26`; metal avg `0.0007` n `20`; unknown avg `2.7716` n `947`
- 24h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.8502` n `234`; crypto_major avg `-0.4253` n `8`; equity avg `0.2155` n `141`; fx avg `0.0286` n `6`; index avg `-0.0106` n `26`; metal avg `-0.0071` n `20`; unknown avg `4.4728` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
