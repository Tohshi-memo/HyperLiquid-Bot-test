# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T00:22:27.443316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `12`; crypto_alt avg `0.1015` n `230`; crypto_major avg `0.0103` n `8`; equity avg `0.1631` n `102`; fx avg `-0.0074` n `6`; index avg `0.0036` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0205` n `782`
- 1h: commodity avg `-0.1706` n `12`; crypto_alt avg `0.306` n `230`; crypto_major avg `0.1844` n `8`; equity avg `0.2908` n `102`; fx avg `0.0011` n `6`; index avg `0.0438` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0568` n `782`
- 4h: commodity avg `-0.2839` n `12`; crypto_alt avg `0.4191` n `230`; crypto_major avg `0.4945` n `8`; equity avg `0.5514` n `102`; fx avg `-0.0268` n `6`; index avg `0.0805` n `25`; metal avg `0.0419` n `20`; unknown avg `0.3156` n `782`
- 24h: commodity avg `-0.2857` n `12`; crypto_alt avg `-0.4692` n `230`; crypto_major avg `-0.6338` n `8`; equity avg `0.1122` n `102`; fx avg `-0.0545` n `6`; index avg `0.0297` n `25`; metal avg `0.0637` n `20`; unknown avg `-0.0362` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
