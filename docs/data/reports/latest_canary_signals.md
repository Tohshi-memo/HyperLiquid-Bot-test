# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T23:38:03.521523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `0.0266` n `234`; crypto_major avg `-0.0555` n `8`; equity avg `0.0039` n `140`; fx avg `0.0126` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0087` n `20`; unknown avg `0.1086` n `919`
- 1h: commodity avg `-0.0149` n `12`; crypto_alt avg `0.5396` n `234`; crypto_major avg `0.2442` n `8`; equity avg `0.0468` n `140`; fx avg `0.0086` n `6`; index avg `0.0024` n `26`; metal avg `0.0154` n `20`; unknown avg `0.6451` n `897`
- 4h: commodity avg `0.0065` n `12`; crypto_alt avg `0.7122` n `234`; crypto_major avg `0.4638` n `8`; equity avg `0.0435` n `140`; fx avg `0.0049` n `6`; index avg `-0.0345` n `26`; metal avg `0.022` n `20`; unknown avg `0.2034` n `791`
- 24h: commodity avg `-0.1885` n `12`; crypto_alt avg `3.6338` n `234`; crypto_major avg `2.0233` n `8`; equity avg `1.7729` n `138`; fx avg `0.0145` n `6`; index avg `0.3337` n `26`; metal avg `0.5496` n `20`; unknown avg `2.3331` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
