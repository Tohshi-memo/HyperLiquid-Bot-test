# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T10:52:37.544141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0455` n `12`; crypto_alt avg `-0.01` n `230`; crypto_major avg `0.0643` n `8`; equity avg `-0.0306` n `102`; fx avg `0.0064` n `6`; index avg `-0.0217` n `25`; metal avg `0.0018` n `20`; unknown avg `0.3627` n `780`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `0.076` n `230`; crypto_major avg `0.1609` n `8`; equity avg `0.0889` n `102`; fx avg `0.0255` n `6`; index avg `0.0299` n `25`; metal avg `0.0323` n `20`; unknown avg `0.5011` n `780`
- 4h: commodity avg `0.3436` n `12`; crypto_alt avg `-0.3634` n `230`; crypto_major avg `-0.6581` n `8`; equity avg `0.528` n `102`; fx avg `0.0802` n `6`; index avg `0.0661` n `25`; metal avg `-0.1131` n `20`; unknown avg `0.3954` n `779`
- 24h: commodity avg `0.2601` n `12`; crypto_alt avg `-0.1695` n `230`; crypto_major avg `-0.1914` n `8`; equity avg `7.5226` n `102`; fx avg `-0.1073` n `6`; index avg `1.0957` n `25`; metal avg `0.0729` n `20`; unknown avg `0.4481` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
