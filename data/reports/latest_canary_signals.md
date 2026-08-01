# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T15:14:07.059293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `0.0049` n `230`; crypto_major avg `0.0704` n `8`; equity avg `-0.0166` n `102`; fx avg `0.002` n `6`; index avg `-0.0175` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0514` n `782`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.0424` n `230`; crypto_major avg `0.075` n `8`; equity avg `0.0016` n `102`; fx avg `-0.0016` n `6`; index avg `0.003` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0072` n `782`
- 4h: commodity avg `0.0134` n `12`; crypto_alt avg `0.172` n `230`; crypto_major avg `0.2427` n `8`; equity avg `-0.0965` n `102`; fx avg `-0.0245` n `6`; index avg `-0.0327` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.1155` n `781`
- 24h: commodity avg `0.3699` n `12`; crypto_alt avg `0.4296` n `230`; crypto_major avg `-0.309` n `8`; equity avg `-0.8255` n `102`; fx avg `-0.0379` n `6`; index avg `-0.0424` n `25`; metal avg `0.0472` n `20`; unknown avg `4.2408` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
