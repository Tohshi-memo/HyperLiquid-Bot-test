# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T13:52:30.247267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0624` n `12`; crypto_alt avg `-0.4496` n `234`; crypto_major avg `-0.4194` n `8`; equity avg `-0.2463` n `141`; fx avg `-0.0109` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0152` n `20`; unknown avg `1.3489` n `944`
- 1h: commodity avg `-0.0894` n `12`; crypto_alt avg `-0.625` n `234`; crypto_major avg `-0.8408` n `8`; equity avg `-0.5647` n `141`; fx avg `-0.0726` n `6`; index avg `-0.0107` n `26`; metal avg `-0.1047` n `20`; unknown avg `450.3043` n `942`
- 4h: commodity avg `-0.1294` n `12`; crypto_alt avg `0.1375` n `234`; crypto_major avg `0.083` n `8`; equity avg `-0.6242` n `141`; fx avg `-0.0674` n `6`; index avg `-0.0313` n `26`; metal avg `-0.0486` n `20`; unknown avg `10.4515` n `936`
- 24h: commodity avg `-0.0388` n `12`; crypto_alt avg `3.2623` n `234`; crypto_major avg `1.7933` n `8`; equity avg `0.8992` n `141`; fx avg `-0.2491` n `6`; index avg `0.2019` n `26`; metal avg `0.0817` n `20`; unknown avg `12.0532` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
