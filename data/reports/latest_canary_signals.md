# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T23:07:30.813141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `13`; crypto_alt avg `-0.3008` n `235`; crypto_major avg `-0.2823` n `8`; equity avg `-0.1399` n `151`; fx avg `0.0229` n `6`; index avg `-0.039` n `26`; metal avg `-0.0317` n `20`; unknown avg `1.5196` n `1133`
- 1h: commodity avg `-0.0138` n `13`; crypto_alt avg `-0.2468` n `235`; crypto_major avg `-0.178` n `8`; equity avg `0.0262` n `151`; fx avg `0.0231` n `6`; index avg `-0.0054` n `26`; metal avg `-0.0241` n `20`; unknown avg `0.3747` n `1133`
- 4h: commodity avg `0.1047` n `13`; crypto_alt avg `-0.2807` n `235`; crypto_major avg `-0.3243` n `8`; equity avg `0.4008` n `151`; fx avg `-0.0052` n `6`; index avg `0.0123` n `26`; metal avg `-0.0436` n `20`; unknown avg `1.6868` n `1019`
- 24h: commodity avg `0.7435` n `13`; crypto_alt avg `0.5717` n `235`; crypto_major avg `0.9882` n `8`; equity avg `-0.2818` n `151`; fx avg `0.1844` n `6`; index avg `-0.1267` n `26`; metal avg `-0.274` n `20`; unknown avg `0.0689` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1565`, n `667`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1426`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0928`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0917`, n `667`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0851`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0812`, n `667`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0805`, n `669`, weak_sample_signal
