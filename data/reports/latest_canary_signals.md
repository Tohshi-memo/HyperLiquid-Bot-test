# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T09:52:28.575606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0652` n `12`; crypto_alt avg `0.0371` n `230`; crypto_major avg `-0.018` n `8`; equity avg `0.0974` n `100`; fx avg `-0.0004` n `6`; index avg `0.0086` n `25`; metal avg `0.0346` n `20`; unknown avg `0.0817` n `775`
- 1h: commodity avg `-0.174` n `12`; crypto_alt avg `0.0867` n `230`; crypto_major avg `0.1183` n `8`; equity avg `0.1949` n `100`; fx avg `-0.021` n `6`; index avg `0.0256` n `25`; metal avg `0.053` n `20`; unknown avg `0.0531` n `775`
- 4h: commodity avg `-0.5604` n `12`; crypto_alt avg `-0.3261` n `230`; crypto_major avg `-0.0046` n `8`; equity avg `0.517` n `100`; fx avg `-0.0168` n `6`; index avg `0.0717` n `25`; metal avg `0.1782` n `20`; unknown avg `0.0199` n `759`
- 24h: commodity avg `-0.9769` n `12`; crypto_alt avg `0.6329` n `230`; crypto_major avg `1.2717` n `8`; equity avg `1.579` n `100`; fx avg `0.1038` n `6`; index avg `0.2131` n `25`; metal avg `0.4401` n `20`; unknown avg `-0.0499` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1953`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
