# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T00:37:27.386329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `0.5403` n `228`; crypto_major avg `0.5647` n `8`; equity avg `0.2067` n `78`; fx avg `0.0073` n `6`; index avg `0.108` n `23`; metal avg `0.0694` n `18`; unknown avg `2.0404` n `702`
- 1h: commodity avg `-0.1002` n `12`; crypto_alt avg `1.0979` n `228`; crypto_major avg `1.0014` n `8`; equity avg `-0.0978` n `78`; fx avg `0.0364` n `6`; index avg `0.1027` n `23`; metal avg `0.3237` n `18`; unknown avg `2.1976` n `702`
- 4h: commodity avg `-0.1828` n `12`; crypto_alt avg `-0.4976` n `228`; crypto_major avg `-0.3566` n `8`; equity avg `-0.7905` n `78`; fx avg `0.0273` n `6`; index avg `-0.062` n `23`; metal avg `0.201` n `18`; unknown avg `0.5541` n `702`
- 24h: commodity avg `0.0347` n `12`; crypto_alt avg `0.0497` n `228`; crypto_major avg `-0.7337` n `8`; equity avg `-0.6748` n `78`; fx avg `-0.0931` n `6`; index avg `-0.047` n `23`; metal avg `0.0978` n `18`; unknown avg `1.2039` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
