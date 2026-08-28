# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T11:52:27.949247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0369` n `12`; crypto_alt avg `-0.0188` n `231`; crypto_major avg `-0.0723` n `8`; equity avg `-0.0947` n `127`; fx avg `-0.0007` n `6`; index avg `-0.0057` n `26`; metal avg `0.0006` n `20`; unknown avg `0.2474` n `792`
- 1h: commodity avg `-0.1896` n `12`; crypto_alt avg `0.2332` n `231`; crypto_major avg `0.1163` n `8`; equity avg `-0.1085` n `127`; fx avg `-0.0034` n `6`; index avg `0.0039` n `26`; metal avg `0.0585` n `20`; unknown avg `0.1564` n `792`
- 4h: commodity avg `-0.0679` n `12`; crypto_alt avg `0.1782` n `231`; crypto_major avg `-0.3504` n `8`; equity avg `-0.1597` n `127`; fx avg `0.0567` n `6`; index avg `-0.0265` n `26`; metal avg `0.1461` n `20`; unknown avg `0.1457` n `792`
- 24h: commodity avg `-0.0579` n `12`; crypto_alt avg `-0.073` n `231`; crypto_major avg `0.2101` n `8`; equity avg `-0.8183` n `127`; fx avg `-0.0166` n `6`; index avg `-0.0013` n `26`; metal avg `0.707` n `20`; unknown avg `0.6264` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
