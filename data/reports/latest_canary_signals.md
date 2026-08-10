# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T01:37:27.626483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0384` n `12`; crypto_alt avg `-0.0927` n `230`; crypto_major avg `-0.1943` n `8`; equity avg `-0.1938` n `112`; fx avg `0.0029` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0665` n `20`; unknown avg `0.2073` n `785`
- 1h: commodity avg `0.0531` n `12`; crypto_alt avg `0.0554` n `230`; crypto_major avg `-0.0093` n `8`; equity avg `-0.101` n `112`; fx avg `0.0368` n `6`; index avg `0.0225` n `25`; metal avg `-0.1417` n `20`; unknown avg `-0.0912` n `785`
- 4h: commodity avg `0.2799` n `12`; crypto_alt avg `-0.8066` n `230`; crypto_major avg `-0.8856` n `8`; equity avg `-0.4513` n `112`; fx avg `0.1083` n `6`; index avg `-0.0082` n `25`; metal avg `-0.2929` n `20`; unknown avg `0.6914` n `785`
- 24h: commodity avg `0.4786` n `12`; crypto_alt avg `0.8076` n `230`; crypto_major avg `-0.2749` n `8`; equity avg `-0.1605` n `112`; fx avg `0.1003` n `6`; index avg `0.028` n `25`; metal avg `-0.2781` n `20`; unknown avg `-0.299` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
