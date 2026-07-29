# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T22:37:32.928747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `12`; crypto_alt avg `-0.0989` n `230`; crypto_major avg `-0.1153` n `8`; equity avg `0.1388` n `102`; fx avg `0.0077` n `6`; index avg `0.033` n `25`; metal avg `0.0184` n `20`; unknown avg `0.8255` n `778`
- 1h: commodity avg `-0.1581` n `12`; crypto_alt avg `0.4535` n `230`; crypto_major avg `0.4864` n `8`; equity avg `1.4342` n `102`; fx avg `0.0262` n `6`; index avg `0.245` n `25`; metal avg `0.1501` n `20`; unknown avg `1.8358` n `778`
- 4h: commodity avg `-0.0752` n `12`; crypto_alt avg `-0.4964` n `230`; crypto_major avg `-0.438` n `8`; equity avg `-1.7599` n `102`; fx avg `0.0796` n `6`; index avg `-0.3938` n `25`; metal avg `0.0623` n `20`; unknown avg `0.1362` n `778`
- 24h: commodity avg `0.5501` n `12`; crypto_alt avg `-2.3339` n `230`; crypto_major avg `-0.4746` n `8`; equity avg `-3.425` n `102`; fx avg `0.0477` n `6`; index avg `-0.5672` n `25`; metal avg `0.3862` n `20`; unknown avg `-0.6513` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
