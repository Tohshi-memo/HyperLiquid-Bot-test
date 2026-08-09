# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T05:16:01.519420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.1375` n `230`; crypto_major avg `-0.0149` n `8`; equity avg `-0.003` n `112`; fx avg `-0.0057` n `6`; index avg `-0.0069` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.0741` n `784`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `-0.2234` n `230`; crypto_major avg `-0.0822` n `8`; equity avg `0.0256` n `112`; fx avg `-0.0016` n `6`; index avg `0.0039` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.0877` n `784`
- 4h: commodity avg `0.1024` n `12`; crypto_alt avg `0.093` n `230`; crypto_major avg `-0.2016` n `8`; equity avg `-0.0838` n `112`; fx avg `0.0019` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0116` n `20`; unknown avg `-0.2059` n `784`
- 24h: commodity avg `0.3096` n `12`; crypto_alt avg `1.5335` n `230`; crypto_major avg `0.4835` n `8`; equity avg `0.5601` n `112`; fx avg `-0.0073` n `6`; index avg `0.0697` n `25`; metal avg `0.0265` n `20`; unknown avg `-0.0216` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
