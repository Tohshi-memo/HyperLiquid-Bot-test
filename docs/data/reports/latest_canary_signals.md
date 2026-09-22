# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T23:03:17.297706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `-0.0028` n `234`; crypto_major avg `0.022` n `8`; equity avg `-0.0058` n `140`; fx avg `0.0021` n `6`; index avg `0.0017` n `26`; metal avg `0.0123` n `20`; unknown avg `0.3971` n `943`
- 1h: commodity avg `-0.0127` n `12`; crypto_alt avg `0.8716` n `234`; crypto_major avg `0.4341` n `8`; equity avg `0.0445` n `140`; fx avg `0.0167` n `6`; index avg `0.0088` n `26`; metal avg `0.0167` n `20`; unknown avg `0.2836` n `943`
- 4h: commodity avg `-0.0428` n `12`; crypto_alt avg `1.1052` n `234`; crypto_major avg `-0.009` n `8`; equity avg `0.1695` n `140`; fx avg `-0.0197` n `6`; index avg `0.0207` n `26`; metal avg `0.0398` n `20`; unknown avg `0.3824` n `906`
- 24h: commodity avg `0.1677` n `12`; crypto_alt avg `2.3172` n `234`; crypto_major avg `-0.1638` n `8`; equity avg `0.709` n `140`; fx avg `-0.2781` n `6`; index avg `0.095` n `26`; metal avg `0.2007` n `20`; unknown avg `1.5584` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
