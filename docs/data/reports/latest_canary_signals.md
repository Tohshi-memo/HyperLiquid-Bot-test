# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T08:43:46.937799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1158` n `12`; crypto_alt avg `-0.0851` n `230`; crypto_major avg `0.0152` n `8`; equity avg `0.1085` n `100`; fx avg `-0.0055` n `6`; index avg `0.0389` n `25`; metal avg `0.0388` n `20`; unknown avg `-0.06` n `775`
- 1h: commodity avg `-0.1749` n `12`; crypto_alt avg `-0.2871` n `230`; crypto_major avg `-0.0788` n `8`; equity avg `0.0638` n `100`; fx avg `0.0172` n `6`; index avg `0.0274` n `25`; metal avg `-0.0545` n `20`; unknown avg `-0.1069` n `775`
- 4h: commodity avg `-0.411` n `12`; crypto_alt avg `-0.3443` n `230`; crypto_major avg `-0.0338` n `8`; equity avg `0.6426` n `100`; fx avg `0.0135` n `6`; index avg `0.1336` n `25`; metal avg `0.1559` n `20`; unknown avg `0.0124` n `759`
- 24h: commodity avg `-0.9076` n `12`; crypto_alt avg `0.48` n `230`; crypto_major avg `1.3581` n `8`; equity avg `1.5134` n `100`; fx avg `0.1256` n `6`; index avg `0.2011` n `25`; metal avg `0.4569` n `20`; unknown avg `-0.0665` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
