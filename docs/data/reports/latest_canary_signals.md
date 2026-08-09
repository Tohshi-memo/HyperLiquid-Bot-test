# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T15:07:32.469580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.1253` n `230`; crypto_major avg `0.1579` n `8`; equity avg `0.0421` n `112`; fx avg `0.007` n `6`; index avg `0.0135` n `25`; metal avg `0.013` n `20`; unknown avg `0.1099` n `785`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.1777` n `230`; crypto_major avg `0.1344` n `8`; equity avg `0.0592` n `112`; fx avg `0.007` n `6`; index avg `0.0078` n `25`; metal avg `0.0159` n `20`; unknown avg `0.1188` n `785`
- 4h: commodity avg `-0.0971` n `12`; crypto_alt avg `0.6055` n `230`; crypto_major avg `0.4588` n `8`; equity avg `0.1741` n `112`; fx avg `0.0079` n `6`; index avg `0.0288` n `25`; metal avg `0.0278` n `20`; unknown avg `0.0712` n `785`
- 24h: commodity avg `0.1757` n `12`; crypto_alt avg `1.1563` n `230`; crypto_major avg `0.0914` n `8`; equity avg `0.4133` n `112`; fx avg `-0.0008` n `6`; index avg `0.0389` n `25`; metal avg `0.0828` n `20`; unknown avg `0.4215` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
