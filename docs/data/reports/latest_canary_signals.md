# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T09:22:31.392714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `0.0259` n `231`; crypto_major avg `0.0203` n `8`; equity avg `0.0057` n `127`; fx avg `0.0039` n `6`; index avg `-0.0002` n `26`; metal avg `0.0101` n `20`; unknown avg `-0.0207` n `793`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `-0.1446` n `231`; crypto_major avg `-0.0015` n `8`; equity avg `-0.0042` n `127`; fx avg `-0.0027` n `6`; index avg `-0.003` n `26`; metal avg `0.0161` n `20`; unknown avg `-0.0469` n `793`
- 4h: commodity avg `0.0165` n `12`; crypto_alt avg `-0.7774` n `231`; crypto_major avg `-0.4525` n `8`; equity avg `0.0299` n `127`; fx avg `-0.0033` n `6`; index avg `-0.0167` n `26`; metal avg `0.014` n `20`; unknown avg `-0.0547` n `761`
- 24h: commodity avg `-0.031` n `12`; crypto_alt avg `-2.2081` n `231`; crypto_major avg `-2.2118` n `8`; equity avg `-1.3414` n `127`; fx avg `-0.0195` n `6`; index avg `-0.1312` n `26`; metal avg `-0.6398` n `20`; unknown avg `-0.4408` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
