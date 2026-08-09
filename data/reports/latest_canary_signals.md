# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T13:52:27.050086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.0542` n `230`; crypto_major avg `-0.0099` n `8`; equity avg `-0.0087` n `112`; fx avg `0.0013` n `6`; index avg `0.0127` n `25`; metal avg `-0.0105` n `20`; unknown avg `0.0017` n `785`
- 1h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.2081` n `230`; crypto_major avg `0.2998` n `8`; equity avg `0.0356` n `112`; fx avg `-0.005` n `6`; index avg `0.0047` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0718` n `785`
- 4h: commodity avg `-0.1263` n `12`; crypto_alt avg `0.2847` n `230`; crypto_major avg `0.3044` n `8`; equity avg `0.0698` n `112`; fx avg `-0.0049` n `6`; index avg `0.0135` n `25`; metal avg `-0.0002` n `20`; unknown avg `0.1489` n `785`
- 24h: commodity avg `0.0744` n `12`; crypto_alt avg `1.3168` n `230`; crypto_major avg `0.3978` n `8`; equity avg `0.3462` n `112`; fx avg `-0.0134` n `6`; index avg `0.0331` n `25`; metal avg `0.0492` n `20`; unknown avg `0.4057` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
