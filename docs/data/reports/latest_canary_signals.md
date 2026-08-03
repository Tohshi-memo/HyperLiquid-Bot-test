# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T07:23:31.213752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0583` n `12`; crypto_alt avg `0.0209` n `230`; crypto_major avg `-0.0183` n `8`; equity avg `-0.0416` n `102`; fx avg `-0.012` n `6`; index avg `-0.0218` n `25`; metal avg `-0.0208` n `20`; unknown avg `-0.0109` n `784`
- 1h: commodity avg `0.0259` n `12`; crypto_alt avg `-0.2525` n `230`; crypto_major avg `-0.3185` n `8`; equity avg `-0.2196` n `102`; fx avg `0.0216` n `6`; index avg `-0.0359` n `25`; metal avg `-0.2063` n `20`; unknown avg `-0.0436` n `784`
- 4h: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.2586` n `230`; crypto_major avg `-0.454` n `8`; equity avg `-0.2474` n `102`; fx avg `-0.0099` n `6`; index avg `-0.0305` n `25`; metal avg `-0.0574` n `20`; unknown avg `0.0002` n `768`
- 24h: commodity avg `-0.1784` n `12`; crypto_alt avg `-1.2184` n `230`; crypto_major avg `-0.9226` n `8`; equity avg `0.5703` n `102`; fx avg `-0.1819` n `6`; index avg `-0.0434` n `25`; metal avg `-0.1605` n `20`; unknown avg `0.9292` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
