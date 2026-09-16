# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T05:22:30.231491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.1863` n `234`; crypto_major avg `0.2355` n `8`; equity avg `0.0131` n `137`; fx avg `0.0125` n `6`; index avg `0.0064` n `27`; metal avg `0.013` n `20`; unknown avg `0.2153` n `919`
- 1h: commodity avg `0.0466` n `12`; crypto_alt avg `-0.2083` n `234`; crypto_major avg `-0.2144` n `8`; equity avg `-0.1908` n `137`; fx avg `0.0211` n `6`; index avg `-0.0314` n `27`; metal avg `-0.0149` n `20`; unknown avg `2.4838` n `911`
- 4h: commodity avg `-0.0732` n `12`; crypto_alt avg `0.0865` n `234`; crypto_major avg `0.1238` n `8`; equity avg `0.5734` n `137`; fx avg `-0.032` n `6`; index avg `0.0641` n `27`; metal avg `0.2515` n `20`; unknown avg `1.9682` n `907`
- 24h: commodity avg `0.1618` n `12`; crypto_alt avg `-2.8294` n `234`; crypto_major avg `-2.7182` n `8`; equity avg `-0.1485` n `137`; fx avg `0.1782` n `6`; index avg `0.0818` n `27`; metal avg `0.4267` n `20`; unknown avg `18796.4154` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
