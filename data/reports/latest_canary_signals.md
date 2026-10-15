# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T11:07:30.879773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `13`; crypto_alt avg `-0.0708` n `236`; crypto_major avg `0.0354` n `8`; equity avg `-0.2927` n `151`; fx avg `0.0077` n `6`; index avg `-0.0321` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.029` n `1134`
- 1h: commodity avg `0.0389` n `13`; crypto_alt avg `-0.4421` n `236`; crypto_major avg `-0.294` n `8`; equity avg `-0.5386` n `151`; fx avg `0.0086` n `6`; index avg `-0.0468` n `26`; metal avg `-0.0448` n `20`; unknown avg `-0.2689` n `1086`
- 4h: commodity avg `0.0262` n `13`; crypto_alt avg `0.2853` n `236`; crypto_major avg `0.156` n `8`; equity avg `-0.6995` n `151`; fx avg `0.0607` n `6`; index avg `-0.0288` n `26`; metal avg `0.1653` n `20`; unknown avg `4.2724` n `1038`
- 24h: commodity avg `-0.4274` n `13`; crypto_alt avg `-4.6327` n `236`; crypto_major avg `-3.5369` n `8`; equity avg `-6.2288` n `151`; fx avg `0.0622` n `6`; index avg `-0.9833` n `26`; metal avg `-0.3679` n `20`; unknown avg `1.6037` n `957`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1194`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1045`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0874`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0866`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0657`, n `666`, weak_sample_signal
