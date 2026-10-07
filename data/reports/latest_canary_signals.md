# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T20:07:34.592293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `13`; crypto_alt avg `0.0491` n `235`; crypto_major avg `0.0817` n `8`; equity avg `-0.0203` n `150`; fx avg `0.0005` n `6`; index avg `-0.0044` n `26`; metal avg `0.0122` n `20`; unknown avg `0.2522` n `1049`
- 1h: commodity avg `-0.0234` n `13`; crypto_alt avg `0.2684` n `235`; crypto_major avg `0.023` n `8`; equity avg `0.0592` n `150`; fx avg `0.0075` n `6`; index avg `0.0156` n `26`; metal avg `0.0028` n `20`; unknown avg `1.4352` n `1049`
- 4h: commodity avg `0.038` n `13`; crypto_alt avg `-0.1007` n `235`; crypto_major avg `-0.5323` n `8`; equity avg `-0.037` n `150`; fx avg `-0.0057` n `6`; index avg `0.0148` n `26`; metal avg `-0.128` n `20`; unknown avg `2.2533` n `1048`
- 24h: commodity avg `0.3076` n `13`; crypto_alt avg `-4.3132` n `235`; crypto_major avg `-3.4465` n `8`; equity avg `-1.3743` n `150`; fx avg `-0.1651` n `6`; index avg `-0.2027` n `26`; metal avg `-0.7475` n `20`; unknown avg `16.1271` n `976`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
