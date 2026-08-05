# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T12:21:00.731625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.3136` n `230`; crypto_major avg `0.4303` n `8`; equity avg `0.1251` n `108`; fx avg `-0.0129` n `6`; index avg `0.0239` n `25`; metal avg `0.0467` n `20`; unknown avg `0.0786` n `782`
- 1h: commodity avg `-0.093` n `12`; crypto_alt avg `0.2451` n `230`; crypto_major avg `0.331` n `8`; equity avg `-0.0348` n `108`; fx avg `-0.0166` n `6`; index avg `0.0192` n `25`; metal avg `0.1816` n `20`; unknown avg `0.0391` n `782`
- 4h: commodity avg `-0.048` n `12`; crypto_alt avg `0.0956` n `230`; crypto_major avg `0.076` n `8`; equity avg `0.0516` n `108`; fx avg `-0.0207` n `6`; index avg `0.0605` n `25`; metal avg `0.2036` n `20`; unknown avg `0.625` n `781`
- 24h: commodity avg `-0.415` n `12`; crypto_alt avg `0.8623` n `230`; crypto_major avg `0.6047` n `8`; equity avg `1.694` n `108`; fx avg `0.049` n `6`; index avg `0.5171` n `25`; metal avg `0.9792` n `20`; unknown avg `0.0524` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
