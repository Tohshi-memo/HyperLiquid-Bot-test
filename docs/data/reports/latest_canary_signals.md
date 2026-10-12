# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T11:22:24.122617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.046` n `13`; crypto_alt avg `-0.0832` n `235`; crypto_major avg `-0.0876` n `8`; equity avg `0.0428` n `151`; fx avg `-0.0015` n `6`; index avg `0.0164` n `26`; metal avg `-0.0055` n `20`; unknown avg `-0.0078` n `1133`
- 1h: commodity avg `0.1079` n `13`; crypto_alt avg `-0.3083` n `235`; crypto_major avg `-0.1894` n `8`; equity avg `-0.1521` n `151`; fx avg `-0.0152` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0196` n `20`; unknown avg `-0.1854` n `1115`
- 4h: commodity avg `0.3605` n `13`; crypto_alt avg `-1.1795` n `235`; crypto_major avg `-0.9926` n `8`; equity avg `-0.681` n `151`; fx avg `-0.0388` n `6`; index avg `-0.1061` n `26`; metal avg `-0.0427` n `20`; unknown avg `0.0896` n `981`
- 24h: commodity avg `0.0269` n `13`; crypto_alt avg `1.5156` n `235`; crypto_major avg `1.0042` n `8`; equity avg `-1.2441` n `151`; fx avg `-0.1343` n `6`; index avg `-0.1564` n `26`; metal avg `0.02` n `20`; unknown avg `0.6524` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.236`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1968`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
