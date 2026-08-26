# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T06:37:28.435715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.2839` n `231`; crypto_major avg `-0.1863` n `8`; equity avg `0.099` n `122`; fx avg `-0.0009` n `6`; index avg `0.0203` n `25`; metal avg `-0.0408` n `20`; unknown avg `0.2779` n `797`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `-0.2871` n `231`; crypto_major avg `-0.4575` n `8`; equity avg `-0.1202` n `122`; fx avg `-0.0063` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0963` n `20`; unknown avg `0.2813` n `781`
- 4h: commodity avg `0.0792` n `12`; crypto_alt avg `-0.6387` n `231`; crypto_major avg `-0.4564` n `8`; equity avg `-0.0028` n `122`; fx avg `-0.0197` n `6`; index avg `0.0323` n `25`; metal avg `-0.1969` n `20`; unknown avg `0.6807` n `781`
- 24h: commodity avg `-0.5299` n `12`; crypto_alt avg `-2.7443` n `231`; crypto_major avg `-2.6513` n `8`; equity avg `0.5841` n `122`; fx avg `-0.0287` n `6`; index avg `0.0649` n `25`; metal avg `0.0402` n `20`; unknown avg `0.8698` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
