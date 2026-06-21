# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T04:07:26.238526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `-0.068` n `228`; crypto_major avg `-0.1017` n `8`; equity avg `-0.0068` n `78`; fx avg `-0.0989` n `6`; index avg `-0.004` n `23`; metal avg `-0.0043` n `18`; unknown avg `2.3191` n `702`
- 1h: commodity avg `0.0243` n `12`; crypto_alt avg `0.0875` n `228`; crypto_major avg `0.1202` n `8`; equity avg `0.1155` n `78`; fx avg `-0.1051` n `6`; index avg `0.0201` n `23`; metal avg `0.0114` n `18`; unknown avg `-0.1501` n `702`
- 4h: commodity avg `0.0404` n `12`; crypto_alt avg `0.2516` n `228`; crypto_major avg `-0.0546` n `8`; equity avg `0.1603` n `78`; fx avg `0.012` n `6`; index avg `0.011` n `23`; metal avg `0.0169` n `18`; unknown avg `0.7389` n `701`
- 24h: commodity avg `0.2128` n `12`; crypto_alt avg `1.56` n `228`; crypto_major avg `1.532` n `8`; equity avg `0.4103` n `78`; fx avg `-0.0501` n `6`; index avg `0.0167` n `23`; metal avg `-0.0039` n `18`; unknown avg `1.6372` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
