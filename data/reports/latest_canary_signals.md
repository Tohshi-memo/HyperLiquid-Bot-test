# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T12:52:19.292546+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1048` n `12`; crypto_alt avg `-0.0525` n `228`; crypto_major avg `-0.0749` n `8`; equity avg `-0.0374` n `67`; fx avg `0.011` n `6`; index avg `-0.0166` n `23`; metal avg `-0.0578` n `18`; unknown avg `-0.0392` n `405`
- 1h: commodity avg `0.4891` n `12`; crypto_alt avg `0.1142` n `228`; crypto_major avg `0.093` n `8`; equity avg `-0.0619` n `67`; fx avg `0.0081` n `6`; index avg `0.0115` n `23`; metal avg `-0.206` n `18`; unknown avg `-0.0078` n `405`
- 4h: commodity avg `0.1667` n `12`; crypto_alt avg `0.0694` n `228`; crypto_major avg `0.0895` n `8`; equity avg `0.2099` n `67`; fx avg `0.0268` n `6`; index avg `0.0935` n `23`; metal avg `0.0707` n `18`; unknown avg `-0.5076` n `397`
- 24h: commodity avg `0.1836` n `12`; crypto_alt avg `0.8105` n `228`; crypto_major avg `-0.0177` n `8`; equity avg `0.4383` n `67`; fx avg `0.0428` n `6`; index avg `0.0716` n `23`; metal avg `0.6386` n `18`; unknown avg `0.3375` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
