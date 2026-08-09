# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T10:52:30.266328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.0918` n `230`; crypto_major avg `0.006` n `8`; equity avg `-0.0102` n `112`; fx avg `0.0062` n `6`; index avg `-0.0053` n `25`; metal avg `-0.0038` n `20`; unknown avg `0.0029` n `785`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `-0.0505` n `230`; crypto_major avg `0.1115` n `8`; equity avg `-0.0115` n `112`; fx avg `0.0039` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0117` n `20`; unknown avg `0.1121` n `785`
- 4h: commodity avg `0.1034` n `12`; crypto_alt avg `-0.2848` n `230`; crypto_major avg `-0.0502` n `8`; equity avg `-0.0868` n `112`; fx avg `-0.0014` n `6`; index avg `-0.0132` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.0319` n `785`
- 24h: commodity avg `0.2756` n `12`; crypto_alt avg `1.1189` n `230`; crypto_major avg `0.3435` n `8`; equity avg `0.4257` n `112`; fx avg `0.002` n `6`; index avg `0.0455` n `25`; metal avg `0.0013` n `20`; unknown avg `0.2792` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0426`, n `668`, weak_sample_signal
