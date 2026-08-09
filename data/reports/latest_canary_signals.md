# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T16:07:26.529791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `0.0846` n `230`; crypto_major avg `0.0885` n `8`; equity avg `0.0127` n `112`; fx avg `0.0001` n `6`; index avg `0.0047` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0338` n `785`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `0.2919` n `230`; crypto_major avg `0.1912` n `8`; equity avg `-0.0326` n `112`; fx avg `0.0029` n `6`; index avg `-0.0019` n `25`; metal avg `0.0114` n `20`; unknown avg `-0.0838` n `785`
- 4h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.9132` n `230`; crypto_major avg `0.808` n `8`; equity avg `0.1501` n `112`; fx avg `0.0031` n `6`; index avg `0.0293` n `25`; metal avg `0.0544` n `20`; unknown avg `0.1358` n `785`
- 24h: commodity avg `0.1733` n `12`; crypto_alt avg `1.1292` n `230`; crypto_major avg `0.1851` n `8`; equity avg `0.3511` n `112`; fx avg `0.0061` n `6`; index avg `0.0183` n `25`; metal avg `0.085` n `20`; unknown avg `0.4031` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
