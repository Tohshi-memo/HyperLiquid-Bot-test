# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T06:52:32.628173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1033` n `13`; crypto_alt avg `0.0666` n `234`; crypto_major avg `0.0877` n `8`; equity avg `-0.0758` n `142`; fx avg `0.0011` n `6`; index avg `-0.0302` n `26`; metal avg `-0.0449` n `20`; unknown avg `0.1056` n `974`
- 1h: commodity avg `0.2167` n `13`; crypto_alt avg `0.1475` n `234`; crypto_major avg `0.0196` n `8`; equity avg `-0.0171` n `142`; fx avg `-0.0253` n `6`; index avg `-0.0356` n `26`; metal avg `-0.1016` n `20`; unknown avg `-0.0073` n `946`
- 4h: commodity avg `-0.1222` n `13`; crypto_alt avg `0.9646` n `234`; crypto_major avg `0.8236` n `8`; equity avg `0.7768` n `142`; fx avg `-0.0235` n `6`; index avg `0.1234` n `26`; metal avg `0.117` n `20`; unknown avg `0.7009` n `940`
- 24h: commodity avg `-0.154` n `13`; crypto_alt avg `2.1016` n `234`; crypto_major avg `1.9031` n `8`; equity avg `1.1382` n `142`; fx avg `0.1448` n `6`; index avg `0.262` n `26`; metal avg `-0.1104` n `20`; unknown avg `776.89` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
