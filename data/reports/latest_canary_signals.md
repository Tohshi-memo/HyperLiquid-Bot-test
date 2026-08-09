# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T15:21:06.254140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.0218` n `230`; crypto_major avg `-0.0672` n `8`; equity avg `-0.0319` n `112`; fx avg `0.0003` n `6`; index avg `-0.0015` n `25`; metal avg `0.0047` n `20`; unknown avg `0.0055` n `785`
- 1h: commodity avg `0.0075` n `12`; crypto_alt avg `0.1358` n `230`; crypto_major avg `0.0906` n `8`; equity avg `0.0098` n `112`; fx avg `0.0093` n `6`; index avg `0.0075` n `25`; metal avg `0.0251` n `20`; unknown avg `0.0604` n `785`
- 4h: commodity avg `-0.0723` n `12`; crypto_alt avg `0.5327` n `230`; crypto_major avg `0.3807` n `8`; equity avg `0.1275` n `112`; fx avg `0.0029` n `6`; index avg `0.0257` n `25`; metal avg `0.0324` n `20`; unknown avg `0.0654` n `785`
- 24h: commodity avg `0.1799` n `12`; crypto_alt avg `1.0972` n `230`; crypto_major avg `0.0697` n `8`; equity avg `0.2765` n `112`; fx avg `-0.0005` n `6`; index avg `0.0234` n `25`; metal avg `0.0833` n `20`; unknown avg `0.3992` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
