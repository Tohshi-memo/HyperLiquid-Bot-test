# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T06:52:34.523487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `0.058` n `234`; crypto_major avg `0.0486` n `8`; equity avg `0.0347` n `140`; fx avg `0.0044` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.1823` n `944`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `0.0588` n `234`; crypto_major avg `0.0275` n `8`; equity avg `-0.1879` n `140`; fx avg `0.0346` n `6`; index avg `-0.0406` n `26`; metal avg `-0.1151` n `20`; unknown avg `0.2139` n `914`
- 4h: commodity avg `0.1042` n `12`; crypto_alt avg `0.2619` n `234`; crypto_major avg `0.2723` n `8`; equity avg `-0.9026` n `140`; fx avg `-0.0003` n `6`; index avg `-0.1105` n `26`; metal avg `-0.209` n `20`; unknown avg `0.2851` n `908`
- 24h: commodity avg `-0.0926` n `12`; crypto_alt avg `2.731` n `234`; crypto_major avg `4.1598` n `8`; equity avg `1.4152` n `140`; fx avg `-0.1765` n `6`; index avg `0.3136` n `26`; metal avg `-0.2009` n `20`; unknown avg `1126.5698` n `792`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
