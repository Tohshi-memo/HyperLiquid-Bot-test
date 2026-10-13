# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T09:22:28.603523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `13`; crypto_alt avg `-0.1351` n `235`; crypto_major avg `-0.0584` n `8`; equity avg `0.028` n `151`; fx avg `0.003` n `6`; index avg `0.0091` n `26`; metal avg `-0.0198` n `20`; unknown avg `0.1576` n `1135`
- 1h: commodity avg `-0.043` n `13`; crypto_alt avg `-0.5955` n `235`; crypto_major avg `-0.6875` n `8`; equity avg `-0.0213` n `151`; fx avg `-0.0418` n `6`; index avg `0.0172` n `26`; metal avg `-0.05` n `20`; unknown avg `0.4217` n `1133`
- 4h: commodity avg `-0.0875` n `13`; crypto_alt avg `-0.8183` n `235`; crypto_major avg `-0.4817` n `8`; equity avg `0.0643` n `151`; fx avg `-0.0475` n `6`; index avg `0.053` n `26`; metal avg `-0.0159` n `20`; unknown avg `1.0732` n `1101`
- 24h: commodity avg `0.0683` n `13`; crypto_alt avg `-3.9505` n `235`; crypto_major avg `-2.2644` n `8`; equity avg `-2.6959` n `151`; fx avg `0.0473` n `6`; index avg `-0.3389` n `26`; metal avg `0.0259` n `20`; unknown avg `0.149` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1843`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1655`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.161`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1407`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0761`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.075`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `666`, weak_sample_signal
