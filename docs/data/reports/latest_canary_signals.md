# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T13:07:25.246475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.1594` n `230`; crypto_major avg `0.1088` n `8`; equity avg `0.0324` n `112`; fx avg `-0.0086` n `6`; index avg `-0.0011` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0184` n `785`
- 1h: commodity avg `0.0068` n `12`; crypto_alt avg `0.2991` n `230`; crypto_major avg `0.1577` n `8`; equity avg `0.0908` n `112`; fx avg `-0.0149` n `6`; index avg `0.0161` n `25`; metal avg `0.0183` n `20`; unknown avg `0.0087` n `785`
- 4h: commodity avg `-0.0616` n `12`; crypto_alt avg `0.3706` n `230`; crypto_major avg `0.1385` n `8`; equity avg `0.0279` n `112`; fx avg `-0.0085` n `6`; index avg `0.0131` n `25`; metal avg `0.0039` n `20`; unknown avg `0.0148` n `785`
- 24h: commodity avg `0.1239` n `12`; crypto_alt avg `1.2102` n `230`; crypto_major avg `0.1454` n `8`; equity avg `0.4512` n `112`; fx avg `-0.0184` n `6`; index avg `0.0406` n `25`; metal avg `0.0464` n `20`; unknown avg `0.2206` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
