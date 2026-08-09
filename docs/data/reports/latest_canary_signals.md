# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T19:52:26.916994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.0976` n `230`; crypto_major avg `0.0018` n `8`; equity avg `0.0232` n `112`; fx avg `-0.0021` n `6`; index avg `-0.0044` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.0176` n `785`
- 1h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.1981` n `230`; crypto_major avg `0.0496` n `8`; equity avg `0.0367` n `112`; fx avg `-0.0064` n `6`; index avg `-0.0049` n `25`; metal avg `0.0242` n `20`; unknown avg `-0.1374` n `785`
- 4h: commodity avg `0.0567` n `12`; crypto_alt avg `0.4652` n `230`; crypto_major avg `-0.1227` n `8`; equity avg `0.1283` n `112`; fx avg `-0.0042` n `6`; index avg `0.0318` n `25`; metal avg `0.0222` n `20`; unknown avg `-0.3356` n `785`
- 24h: commodity avg `0.0904` n `12`; crypto_alt avg `1.3919` n `230`; crypto_major avg `0.1647` n `8`; equity avg `0.1892` n `112`; fx avg `-0.0066` n `6`; index avg `0.0408` n `25`; metal avg `0.0894` n `20`; unknown avg `-0.2279` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
