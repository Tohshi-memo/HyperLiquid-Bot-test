# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T23:07:29.297732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `13`; crypto_alt avg `0.1065` n `239`; crypto_major avg `0.26` n `8`; equity avg `0.2683` n `162`; fx avg `0.01` n `6`; index avg `0.0494` n `27`; metal avg `0.0172` n `20`; unknown avg `0.1725` n `1255`
- 1h: commodity avg `0.0179` n `13`; crypto_alt avg `0.0571` n `239`; crypto_major avg `0.1246` n `8`; equity avg `0.3466` n `162`; fx avg `0.0045` n `6`; index avg `0.0462` n `27`; metal avg `0.0217` n `20`; unknown avg `1.1817` n `1223`
- 4h: commodity avg `0.2289` n `13`; crypto_alt avg `0.7448` n `239`; crypto_major avg `0.489` n `8`; equity avg `0.5113` n `162`; fx avg `0.0097` n `6`; index avg `0.0594` n `27`; metal avg `-0.0045` n `20`; unknown avg `0.9782` n `1187`
- 24h: commodity avg `0.915` n `13`; crypto_alt avg `-0.5365` n `239`; crypto_major avg `-1.4461` n `8`; equity avg `-0.4553` n `162`; fx avg `-0.1234` n `6`; index avg `0.0392` n `27`; metal avg `-0.6495` n `20`; unknown avg `50.8573` n `1119`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
