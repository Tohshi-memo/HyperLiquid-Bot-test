# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T16:52:26.628985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `13`; crypto_alt avg `0.1197` n `235`; crypto_major avg `-0.009` n `8`; equity avg `-0.0319` n `150`; fx avg `0.0` n `6`; index avg `-0.0049` n `26`; metal avg `0.0009` n `20`; unknown avg `1.3228` n `1117`
- 1h: commodity avg `-0.0147` n `13`; crypto_alt avg `0.1943` n `235`; crypto_major avg `-0.198` n `8`; equity avg `-0.0497` n `150`; fx avg `0.0` n `6`; index avg `-0.006` n `26`; metal avg `0.0034` n `20`; unknown avg `13.4234` n `1109`
- 4h: commodity avg `-0.0108` n `13`; crypto_alt avg `1.0454` n `235`; crypto_major avg `0.3837` n `8`; equity avg `0.0698` n `150`; fx avg `-0.0076` n `6`; index avg `0.0118` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.8861` n `1101`
- 24h: commodity avg `-0.3986` n `13`; crypto_alt avg `2.3696` n `235`; crypto_major avg `0.6872` n `8`; equity avg `0.2122` n `150`; fx avg `0.0217` n `6`; index avg `0.0317` n `26`; metal avg `0.0041` n `20`; unknown avg `1.4453` n `992`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
