# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T01:22:26.542524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `13`; crypto_alt avg `0.0552` n `235`; crypto_major avg `0.0259` n `8`; equity avg `-0.0781` n `151`; fx avg `0.0006` n `6`; index avg `-0.0174` n `26`; metal avg `-0.0606` n `20`; unknown avg `0.0409` n `1135`
- 1h: commodity avg `0.1084` n `13`; crypto_alt avg `-0.1964` n `235`; crypto_major avg `0.0061` n `8`; equity avg `-0.1476` n `151`; fx avg `0.0567` n `6`; index avg `-0.0347` n `26`; metal avg `-0.0679` n `20`; unknown avg `0.9389` n `1139`
- 4h: commodity avg `0.1632` n `13`; crypto_alt avg `0.2215` n `235`; crypto_major avg `0.1822` n `8`; equity avg `0.0126` n `151`; fx avg `0.0352` n `6`; index avg `-0.0364` n `26`; metal avg `-0.0984` n `20`; unknown avg `0.3372` n `1071`
- 24h: commodity avg `1.028` n `13`; crypto_alt avg `1.7733` n `235`; crypto_major avg `1.6781` n `8`; equity avg `0.6474` n `151`; fx avg `0.1542` n `6`; index avg `0.0737` n `26`; metal avg `-0.2731` n `20`; unknown avg `0.9373` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1562`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1429`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1111`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0971`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0756`, n `666`, weak_sample_signal
