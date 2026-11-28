# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T20:07:28.034781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `13`; crypto_alt avg `0.1754` n `239`; crypto_major avg `-0.002` n `8`; equity avg `0.0651` n `168`; fx avg `-0.0008` n `6`; index avg `0.0057` n `27`; metal avg `0.0077` n `20`; unknown avg `4.3839` n `1240`
- 1h: commodity avg `0.001` n `13`; crypto_alt avg `0.0686` n `239`; crypto_major avg `-0.0843` n `8`; equity avg `0.0872` n `168`; fx avg `-0.0232` n `6`; index avg `0.007` n `27`; metal avg `0.0185` n `20`; unknown avg `4.2809` n `1246`
- 4h: commodity avg `0.0831` n `13`; crypto_alt avg `-0.1386` n `239`; crypto_major avg `-0.2054` n `8`; equity avg `0.2143` n `168`; fx avg `-0.0206` n `6`; index avg `0.0197` n `27`; metal avg `0.0239` n `20`; unknown avg `56.9539` n `1205`
- 24h: commodity avg `-0.0373` n `13`; crypto_alt avg `-3.0324` n `239`; crypto_major avg `-1.3245` n `8`; equity avg `0.0333` n `168`; fx avg `-0.0065` n `6`; index avg `0.0101` n `27`; metal avg `0.0737` n `20`; unknown avg `-0.4295` n `1057`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
