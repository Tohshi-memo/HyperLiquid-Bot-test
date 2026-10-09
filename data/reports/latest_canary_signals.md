# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T07:37:36.069450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0664` n `13`; crypto_alt avg `0.0587` n `235`; crypto_major avg `0.0659` n `8`; equity avg `-0.0211` n `150`; fx avg `0.008` n `6`; index avg `0.003` n `26`; metal avg `-0.0084` n `20`; unknown avg `-0.0644` n `1078`
- 1h: commodity avg `-0.0654` n `13`; crypto_alt avg `0.1759` n `235`; crypto_major avg `0.111` n `8`; equity avg `0.0626` n `150`; fx avg `0.0196` n `6`; index avg `0.0178` n `26`; metal avg `0.0673` n `20`; unknown avg `1.1774` n `1076`
- 4h: commodity avg `-0.0083` n `13`; crypto_alt avg `0.8546` n `235`; crypto_major avg `0.4642` n `8`; equity avg `0.7228` n `150`; fx avg `0.0384` n `6`; index avg `0.0888` n `26`; metal avg `0.1735` n `20`; unknown avg `0.5669` n `1040`
- 24h: commodity avg `-0.279` n `13`; crypto_alt avg `-1.3122` n `235`; crypto_major avg `-2.1626` n `8`; equity avg `-0.5479` n `150`; fx avg `0.1443` n `6`; index avg `0.0399` n `26`; metal avg `0.481` n `20`; unknown avg `6.5844` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
