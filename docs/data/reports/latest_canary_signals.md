# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T08:37:26.595618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `0.0782` n `235`; crypto_major avg `0.166` n `8`; equity avg `-0.1111` n `151`; fx avg `-0.0099` n `6`; index avg `-0.0206` n `26`; metal avg `0.0153` n `20`; unknown avg `1.0448` n `1133`
- 1h: commodity avg `0.2007` n `13`; crypto_alt avg `-0.2426` n `235`; crypto_major avg `-0.2637` n `8`; equity avg `-0.3392` n `151`; fx avg `-0.0357` n `6`; index avg `-0.0334` n `26`; metal avg `-0.1019` n `20`; unknown avg `0.886` n `1059`
- 4h: commodity avg `0.2493` n `13`; crypto_alt avg `-0.5361` n `235`; crypto_major avg `-0.1394` n `8`; equity avg `-0.7136` n `151`; fx avg `-0.0478` n `6`; index avg `-0.1003` n `26`; metal avg `-0.1185` n `20`; unknown avg `1.2885` n `1007`
- 24h: commodity avg `-0.2325` n `13`; crypto_alt avg `2.0647` n `235`; crypto_major avg `1.5963` n `8`; equity avg `-0.8806` n `151`; fx avg `-0.1097` n `6`; index avg `-0.0752` n `26`; metal avg `0.0091` n `20`; unknown avg `0.3532` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
